## 7장 셀레니움을 이용한 웹 스크레이핑

# [7장: 306페이지]
## 7.3 동적 웹 페이지에서 데이터 가져오기
# requests는 정적인 곳에서 가지고와서 html소스가 웹브라우저와 다를수 있음
# 이때 셀레니움을 사용하면됨

# 7.3.1 커피 전문점 음료 메뉴 가져오기


# requests로 해보기

import requests  
from bs4 import BeautifulSoup 

url = "https://www.starbucks.co.kr/menu/drink_list.do"

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

# 요소 검사를 수행한 결과의 상위 태그와 속성을 이용
products = soup.select('li.menuDataSet dl dd') 
products  # Out[2]: []

# 메뉴 이름을 가지고 오지 못함   스벅홈페이지가 자바스크립를 사용하기 때문에
# 셀레니움으로 HTML소스를 모두 가져온 후에 CSS선택자를 이용해 원하는 것을 가지고 와야함

#%%
# 셀레니움 이용
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 

driver = Chrome()

url = "https://www.starbucks.co.kr/menu/drink_list.do" # URL 지정
driver.get(url)                    # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)          # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source          #  접속 후에 .page_source로 해당 page의 HTML 코드를 가져옴
soup = BeautifulSoup(html, 'lxml') # HTML 코드를 파싱함

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력

drink_products = soup.select('li.menuDataSet dl')
#  div.product_list > dl > dd:nth-child(2) > ul > li:nth-child(1) > dl > dd    > 안에 메뉴이름있음
#  div.product_list > dl > dd:nth-child(2) > ul > li:nth-child(3) > dl > dt > a > img  > 안에 그림있음

driver.quit()            # 웹 브라우저 종료

#%%
# 가지고온거 이쁘게 보기
print(drink_products[0].prettify())  # 데이터가 list안에 하나의 덩어리(element.ResultSet)로 들어가서 drink_products[0]

# dd안에 있는 메뉴이름 가지고오기 
drink_menu_name = drink_products[0].select_one('dd').get_text()  # 메뉴이름 뽑아오기
drink_menu_name

# 메뉴사진이 있는 링크 추출
drink_menu_photo_link = drink_menu_name = drink_products[0].select_one('a img')['src']  # 사진 뽑아오기
# drink_menu_photo_link = drink_menu_name = drink_products[0].select_one('a img') 하면
# <img alt="여수 윤슬 헤이즐넛 콜드브루" src="~~링크"/> 로 나옴
print(drink_menu_photo_link)


#%%
# 모든메뉴 가지고 오기

from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 

driver = Chrome()

url = "https://www.starbucks.co.kr/menu/drink_list.do" # URL 지정
driver.get(url)                    # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)          # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source          # 접속 후에 해당 page의 HTML 코드를 가져옴
soup = BeautifulSoup(html, 'lxml') # HTML 코드를 파싱함

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력

drink_products = soup.select('li.menuDataSet dl')

driver.quit()    


# for문을 사용해서 모든 메뉴 가지고 오기
drink_menu_name_photo_links = [] 
for drink_product in drink_products:  # for문으로 하나씩 가지고옴
    menu_name = drink_product.select_one('dd').get_text()  # select_one을 써야지 .get_text()가 먹힘
    menu_photo_link = drink_product.select_one('a img')['src']
    drink_menu_name_photo_links.append((menu_name, menu_photo_link))  # append해서 뽑아온거 한세트로 넣기

# 잘뽑아왔는지 앞에 4개만 확인
drink_menu_name_photo_links[0:4]
# 메뉴개수 확인
len(drink_menu_name_photo_links)

#%%
# 뽑아온거 DataFrame에 넣기
import pandas as pd

col_drink_menu = ["메뉴", "사진"]  # columns이름 만들기
df = pd.DataFrame(drink_menu_name_photo_links, columns=col_drink_menu)
df.head(4)

#%%
# df에 있는 사진 url 순서대로 뽑기
for i in range(len(df)):
    print(df['사진'][i])

# df에 있는 메뉴 순서대로 뽑기    # df.iloc[:, 1].values 이렇게도 가능
for i in range(len(df)):
    print(df['메뉴'][i])

#%%
df.iloc[:, 0]   # 메뉴이름
df.iloc[:, 1]   # url 


#%%
#### html형식으로 만들기
# 뽑아온 이미지링크를 HTML img 태그로 만드는 함수 

def make_HTML_image_tag(link):
    image_width = 80   # 이미지 크기(너비)를 지정
    image_tag = f'<img src="{link}" width="{image_width}">' # img 태그
    return image_tag  # img 태그를 반환

make_HTML_image_tag



# In[ ]:


make_HTML_image_tag(df["사진"][0])


# [7장: 313페이지]

# In[ ]:


html_table = df.head(4).to_html(formatters=dict(사진=make_HTML_image_tag), escape=False)
print(html_table)


# [7장: 314페이지]

# In[ ]:


from IPython.display import HTML

HTML(html_table) # HTML 코드의 내용을 웹 브라우저처럼 보여줌


# [7장: 315페이지]

# In[ ]:


folder = "C:/myPyScraping/data/ch07/"            # 폴더 지정
file_name = folder + "starbucks_drink_menu.html" # 생성할 HTML 파일 이름 지정 

df.to_html(file_name, formatters=dict(사진=make_HTML_image_tag), escape=False)

print("생성한 파일:", file_name)


