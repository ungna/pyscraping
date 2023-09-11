#!/usr/bin/env python
# coding: utf-8

# # 7장 셀레니움을 이용한 웹 스크레이핑

# ## 7.1 셀레니움 소개 및 설치

# ## 7.2 셀레니움으로 웹 브라우저 제어

# ### 7.2.1 웹 사이트 접속

# [7장: 285페이지]

# In[ ]:


from selenium.webdriver import Chrome

driver = Chrome()                   # 크롬 드라이버 객체 생성

driver.set_window_size(800, 600)    # 웹 브라우저의 창 크기 설정
# driver.maximize_window()        

driver.get("https://www.google.com") # 웹 브라우저를 실행해 지정한 URL에 접속

print("- 접속한 웹 사이트의 제목:", driver.title)       # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url)  # 접속한 웹 사이트의 URL 출력


# ### 7.2.2 HTML 코드에서 요소 찾기

# ### 7.2.3 검색창에 문자열 입력하기

# [7장: 289페이지]

# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 800) # 웹 브라우저의 창 크기 설정      

url = "https://www.google.com"   # URL 지정
driver.get(url)                  # 웹 브라우저를 실행해 지정한 URL에 접속

query = "python"
input_element = driver.find_element(By.NAME, "q") # 검색어를 입력할 수 있는 검색창 찾기
input_element.send_keys(query)                    # 검색창에 검색어 입력 
input_element.submit()                            # 검색 결과 요청

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력


# [7장: 291페이지]

# In[ ]:


from selenium.webdriver import Chrome

driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 800) # 웹 브라우저의 창 크기 설정      

url = "https://www.naver.com"    # URL 지정
driver.get(url)  # 웹 브라우저를 실행해 지정한 URL에 접속

query = "파이썬"

# 검색어를 입력할 수 있는 검색창의 찾기
input_element = driver.find_element(By.NAME, "query")   
input_element.send_keys(query)   # 검색창에 검색어 입력 
input_element.submit()           # 검색 결과 요청

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 URL의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url)  # 접속한 URL 출력


# ### 7.2.4 웹 사이트 로그인 자동화

# [7장: 295페이지]

# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()                  # 크롬 드라이버 객체 생성    
driver.set_window_size(800, 900)   # 웹 브라우저의 창 크기 설정

url = "https://accounts.kakao.com" # 카카오 계정 로그인 URL 지정
driver.get(url)                    # 웹 브라우저를 실행해 지정한 URL에 접속

my_id = "kakao_id"                 # 자신의 아이디 입력
my_pw = "kakao_password"           # 자신의 패스워드 입력

# 아이디 입력
# user_id = driver.find_element(By.ID, "id_email_2")    # id 속성으로 아이디(ID) 입력창 찾기 
user_id = driver.find_element(By.NAME, "email")         # name 속성으로 아이디(ID) 입력창 찾기
user_id.send_keys(my_id)                                # 아이디 전송

# 패스워드 입력
# user_pw = driver.find_element(By.ID, "id_password_3") # id 속성으로 패스워드(비밀번호) 입력창 찾기 
user_pw = driver.find_element(By.NAME, "password")      # name 속성으로 패스워드(비밀번호) 입력창 찾기
user_pw.send_keys(my_pw)                                # 패스워드 전송
time.sleep(1)

# 로그인 버튼 클릭하기 
xpath = '//*[@id="login-form"]/fieldset/div[8]/button[1]' # XPath
login_button = driver.find_element(By.XPATH, xpath)       # XPath로 로그인 버튼 찾기
login_button.click()                                      # 버튼 클릭
    
print("- 접속한 웹 사이트의 제목:", driver.title)       # 접속한 URL의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url)  # 접속한 URL 출력


# [7장: 297페이지]

# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 900) # 웹 브라우저의 창 크기 설정

url = "https://nid.naver.com/"   # 네이버 계정 로그인 URL 지정
driver.get(url)                  # 웹 브라우저를 실행해 지정한 URL에 접속

my_id = "naver_id"               # 자신의 아이디 입력
my_pw = "naver_password"         # 자신의 패스워드 입력

# 아이디 입력
script_id = f"document.getElementsByName('id')[0].value='{my_id}'"
driver.execute_script(script_id)  # 자바스크립트로 아이디 입력

# 패스워드 입력
script_pw = f"document.getElementsByName('pw')[0].value='{my_pw}'"
driver.execute_script(script_pw)  # 자바스크립트로 패스워드 입력

time.sleep(1)

# 로그인 버튼 클릭하기 
xpath = '//*[@id="log.login"]'                     # XPath
login_button = driver.find_element(By.XPATH, xpath)# XPath로 로그인 버튼 찾기
login_button.click()                               # 버튼 클릭
    
print("- 접속한 웹 사이트의 제목:", driver.title)  # 접속한 URL의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 URL 출력


# ### 7.2.5 웹 브라우저 스크롤

# [7장: 299페이지]

# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()                  # 크롬 드라이버 객체 생성
driver.set_window_size(1000, 1000) # 웹 브라우저의 창 크기 설정

url = "https://www.google.com"     # URL 지정
driver.get(url)                    # 웹 브라우저를 실행해 지정한 URL에 접속

input_element = driver.find_element(By.NAME, "q") # 검색창 찾기
input_element.clear()              # 검색창 내용 모두 지우기
query = "python"
input_element.send_keys(query)     # 검색창에 검색어 입력
input_element.submit()             # 검색 결과 요청

# 웹 사이트 문서 높이 가져오기
scroll_height = driver.execute_script("return document.body.scrollHeight")
print("- 웹 사이트 문서 높이:", scroll_height)

y = 0         # Y축 좌표의 초깃값
y_step = 200  # Y축 아래로 이동하는 단계

while (True):
    y = y + y_step
    script =  "window.scrollTo(0,{0})".format(y)
    driver.execute_script(script)   # 스크립트 실행
    time.sleep(1)                   # 데이터를 받아올 때까지 기다림
    
    # 수식 스크롤 위치가 문서 끝보다 크거나 같으면 while 문 빠져나가기
    if (y >= scroll_height):
        break


# ### 7.2.6 웹 브라우저 내용을 이미지 파일로 저장

# [7장: 300페이지]

# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 780) # 웹 브라우저의 창 크기 설정

url = "https://www.google.com"   # URL 지정
driver.get(url)                  # 웹 브라우저를 실행해 지정한 URL에 접속

input_element = driver.find_element(By.NAME, "q") # 검색창 찾기
input_element.clear()                   # 검색창 내용 모두 지우기
query = "환율"
input_element.send_keys(query)         # 검색창에 검색어 입력
input_element.submit()                 # 검색 결과 요청

folder = "C:/myPyScraping/data/ch07/" # 폴더 지정
image_file = folder + "환율정보.png"  # 생성할 이미지 파일 이름 지정
driver.save_screenshot(image_file)    # 웹 브라우저 내용을 캡처해 이미지 파일로 저장

time.sleep(3) 
driver.quit()  # 웹 브라우저를 종료함

print("- 생성한 이미지 파일:", image_file) # 접속한 URL의 제목 출력


# [7장: 301페이지]

# In[ ]:


driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 780) # 웹 브라우저의 창 크기 설정
driver.get(image_file)           # 웹 브라우저로 이미지 파일 열기


# ### 7.2.7 헤드리스(Headless) 웹 브라우저 이용하기

# [7장: 303페이지]

# In[ ]:


from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

options = Options()                  # 옵션 설정을 위한 객체 생성
options.add_argument('headless')     # 헤드리스 웹 브라우저로 옵션 설정
options.add_argument('window-size=1100,1000') # 웹 브라우저의 창 크기 설정

driver = Chrome(options=options)     # 옵션을 지정해 크롬 드라이버의 객체 생성

url = "https://finance.naver.com/"   # URL 지정
driver.get(url)                      # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)            # 웹 사이트의 내용을 받아오기까지 기다림

folder = "C:/myPyScraping/data/ch07/"   # 폴더 지정
image_file = folder + "네이버_금융.png" # 생성할 이미지 파일 이름 지정
driver.save_screenshot(image_file)      # 웹 브라우저 내용을 캡처해 이미지 파일로 저장

driver.quit() # 웹 브라우저 종료

print("- 생성한 이미지 파일:", image_file) # 접속한 URL의 제목 출력


# [7장: 304페이지]

# In[ ]:


from IPython.display import Image

Image(filename=image_file)              # 이미지 파일 이름을 지정
# Image(filename=image_file, width=800) # 이미지 파일 이름과 너비를 지정


# ## 7.3 동적 웹 페이지에서 데이터 가져오기

# ### 7.3.1 커피 전문점 음료 메뉴 가져오기

# [7장: 306페이지]

# In[ ]:


import requests  
from bs4 import BeautifulSoup 

url = "https://www.starbucks.co.kr/menu/drink_list.do"

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

# 요소 검사를 수행한 결과의 상위 태그와 속성을 이용
products = soup.select('li.menuDataSet dl dd') 
products


# [7장: 307페이지]

# In[ ]:


products = soup.select('div.product_list dl dd')
products[0:3]


# [7장: 308페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 

driver = Chrome() # 옵션을 지정해 크롬 드라이버의 객체 생성

url = "https://www.starbucks.co.kr/menu/drink_list.do" # URL 지정
driver.get(url)                    # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)          # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source          # 접속 후에 해당 page의 HTML 코드를 가져옴
soup = BeautifulSoup(html, 'lxml') # HTML 코드를 파싱함

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력


# In[ ]:


drink_products = soup.select('div.product_list dl dd ul li.menuDataSet dl')
drink_products[0] # 첫 번째 음료 메뉴의 요소 출력


# [7장: 309페이지]

# In[ ]:


print(drink_products[0].prettify())


# In[ ]:


drink_menu_name = drink_products[0].select_one('dd').get_text()
drink_menu_name


# [7장: 310페이지]

# In[ ]:


drink_menu_photo_link = drink_products[0].select_one('a img')['src']
drink_menu_photo_link


# In[ ]:


from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 
import pandas as pd

options = Options()
options.headless = True # 헤드리스 모드로 지정해 크롬을 GUI 없이 수행

driver = Chrome(options=options) # 옵션을 지정해 크롬 드라이버의 객체 생성

url = "https://www.starbucks.co.kr/menu/drink_list.do"  # URL 지정
driver.get(url)              # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)    # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source    # 접속 후에 해당 page의 HTML 코드를 가져옴
soup = BeautifulSoup(html, 'lxml') # HTML 코드 파싱

drink_products = soup.select('div.product_list dl dd ul li.menuDataSet dl')
driver.quit() # 웹 브라우저를 종료함

drink_menu_name_photo_links = [] 
for drink_product in drink_products:
    menu_name = drink_product.select_one('dd').get_text()
    menu_photo_link = drink_product.select_one('a img')['src']
    drink_menu_name_photo_links.append((menu_name, menu_photo_link))

drink_menu_name_photo_links[0:4]


# [7장: 311페이지]

# In[ ]:


len(drink_menu_name_photo_links) # 스타벅스 음료 메뉴의 개수


# In[ ]:


col_drink_menu = ["메뉴", "사진"]
df = pd.DataFrame(drink_menu_name_photo_links, columns=col_drink_menu)
df.head(4)


# In[ ]:


# 이미지의 링크를 HTML img 태그로 만드는 함수 
def make_HTML_image_tag(link):
    image_width = 80   # 이미지 크기(너비)를 지정
    image_tag = f'<img src="{link}" width="{image_width}">' # img 태그
    return image_tag  # img 태그를 반환


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


# ### 7.3.2 가상 화폐 거래 정보 가져오기

# [7장: 317페이지]

# In[ ]:


import requests
import pandas as pd

url = "http://coinmarketcap.com/ko/" # URL 지정
html = requests.get(url).text        # HTML 소스 가져오기
dfs = pd.read_html(html)             # HTML 소스에서 table의 내용을 DataFrame 리스트로 변환

df = dfs[0]       # 리스트의 첫 번째 요소를 선택
df.iloc[0:12,1:6] # DataFrame 데이터에서 행과 열을 선택해 출력


# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

driver = Chrome()          # 크롬 드라이버 객체 생성

url = "https://coinmarketcap.com/ko/" # URL 지정
driver.get(url)            # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)  # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source  # 접속 후에 해당 page의 HTML 소스를 가져옴
dfs = pd.read_html(html)   # HTML 소스에서 table의 내용을 DataFrame 리스트로 변환

df = dfs[0]       # 리스트의 첫 번째 요소를 선택
df.iloc[0:16,1:6] # DataFrame 데이터에서 행과 열을 선택해 출력


# [7장: 319페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

driver = Chrome() # 크롬 드라이버 객체 생성

url = "https://coinmarketcap.com/ko/" # URL 지정
driver.get(url)  # 웹 브라우저를 실행해 지정한 URL에 접속

# 웹 사이트 문서 높이 가져오기
scroll_height = driver.execute_script("return document.body.scrollHeight")

y = 0          # Y축 좌표의 초깃값
y_step = 1000  # Y축 아래로 이동하는 단계
while (True):
    y = y + y_step
    script =  "window.scrollTo(0,{0})".format(y)
    driver.execute_script(script) # 스크립트 실행
    driver.implicitly_wait(5)     # 스크롤 수행 후 데이터를 받아올 때까지 기다림
    
    # 수식 스크롤 위치가 문서 끝보다 크거나 같으면 while 문 빠져나가기
    if (y >= scroll_height):
        break
    
html = driver.page_source # HTML 코드를 가져옴
dfs = pd.read_html(html)  # HTML 소스에서 table의 내용을 DataFrame 리스트로 변환

df = dfs[0]         # 리스트의 첫 번째 요소를 선택
df.iloc[95:100,1:6] # DataFrame 데이터에서 행과 열을 선택해 출력


# [7장: 320페이지]

# In[ ]:


df.iloc[0:5,1:6]


# In[ ]:


df['이름'] = [name.replace(str(num), " ") for num, name in zip(df['#'], df['이름'])]
df['이름'] = [name.replace("구매하기", "") for name in df['이름']]
df.iloc[0:5,1:6]


# [7장: 321페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

def get_coin_info(page_num):
    driver = Chrome() # 크롬 드라이버 객체 생성
    
    # page 추가해 URL 지정
    url = f"https://coinmarketcap.com/ko/?page={page_num}"
    driver.get(url)  # 웹 브라우저를 실행해 지정한 URL에 접속

    # 웹 사이트 문서 높이 가져오기
    scroll_height = driver.execute_script("return document.body.scrollHeight")

    y = 0           # Y축 좌표의 초깃값
    y_step = 1000   # Y축 아래로 이동하는 단계
    while (True):
        y = y + y_step
        script =  "window.scrollTo(0,{0})".format(y)
        driver.execute_script(script) # 스크립트 실행
        driver.implicitly_wait(5) # 스크롤 수행 후 데이터를 받아올 때까지 기다림

        # 수식 스크롤 위치가 문서 끝보다 크거나 같으면 while 문 빠져나가기
        if (y >= scroll_height):
            break

    html = driver.page_source # HTML 코드를 가져옴
    dfs = pd.read_html(html)  # HTML 소스에서 table의 내용을 DataFrame 리스트로 변환

    df = dfs[0] # 리스트의 첫 번째 요소를 선택
    
    # '이름' 열의 내용 변경
    df['이름'] = [name.replace(str(num), " ") for num, name in zip(df['#'], df['이름'])]
    df['이름'] = [name.replace("구매하기", "") for name in df['이름']]
    
    driver.quit() # 웹 브라우저를 종료함

    return df.iloc[:,1:9]


# [7장: 322페이지]

# In[ ]:


page_num = 1 # page 지정
df_coin = get_coin_info(page_num) # 함수 호출

# DataFrame 데이터에서 행과 열을 선택해 출력
with pd.option_context('display.max_rows',6):
    pd.set_option("show_dimensions", False) # DataFrame의 행과 열 개수 출력 안 하기
    display(df_coin.iloc[:,0:6])


# ### 7.3.3 유튜브 검색 결과 가져오기

# [7장: 324페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time

driver = Chrome() # 크롬 드라이버 객체 생성

base_url = "https://www.youtube.com" # 유튜브의 기본 URL
search_word = '/results?search_query=' + '방탄소년단' # 검색어
url = base_url +  search_word        # 접속하고자 하는 웹 사이트

driver.get(url) # 웹 브라우저를 실행해 지정한 URL에 접속
time.sleep(3)   # 웹 브라우저를 실행하고 URL에 접속할 때까지 기다림

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력


# In[ ]:


driver = Chrome()

base_url = "https://www.youtube.com"
search_word = '/results?search_query=' + '방탄소년단'
search_option = "&sp=CAMSAhAB" # 조회수로 정렬

url = base_url +  search_word + search_option # 접속하고자 하는 웹 사이트
driver.get(url)
time.sleep(3) # 웹 브라우저를 실행하고 URL에 접속할 때까지 기다림


# [7장: 326페이지]

# In[ ]:


html = driver.page_source # 접속 후에 해당 page의 HTML 코드를 가져옴
# driver.quit() # 웹 브라우저를 종료함

soup = BeautifulSoup(html, 'lxml')

title_hrefs = soup.select('a#video-title')

title_hrefs[0] # 첫 번째 항목 출력


# In[ ]:


title_hrefs[0].get('title') # title_hrefs[0]['title'] 도 동일


# In[ ]:


title_hrefs[0]['href'] # title_hrefs[0].get('href')도 동일


# [7장: 327페이지]

# In[ ]:


base_url = "https://www.youtube.com"
titles = []
urls = []
for title_href in title_hrefs[0:5]:
    title = title_href['title']         # 태그 안에서 title 속성의 값을 가져오기
    url = base_url + title_href['href'] # href 속성의 값 가져와 기본 url과 합치기
    titles.append(title)
    urls.append(url)
    print("{0}, {1}".format(title, url))


# [7장: 328페이지]

# In[ ]:


view_uploads = soup.select('span.style-scope.ytd-video-meta-block')

view_uploads[0:6]


# [7장: 329페이지]

# In[ ]:


view_numbers = view_uploads[0::2] # 인덱스가 짝수인 요소 선택
upload_times = view_uploads[1::2] # 인덱스가 홀수인 요소 선택

[view_numbers[0:3], upload_times[0:3]]


# In[ ]:


[view_numbers[0].get_text(), upload_times[0].get_text()]


# In[ ]:


[view_numbers[0].get_text().split(" ")[-1], upload_times[0].get_text()]


# [7장: 330페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 
import pandas as pd
import time

def get_data_from_youtube(word, scroll=False):
    driver = Chrome()

    base_url = "https://www.youtube.com"
    search_word = '/results?search_query=' + word
    search_option = "&sp=CAMSAhAB" # 조회수로 정렬

    url = base_url +  search_word + search_option # 접속하고자 하는 웹 사이트
    driver.get(url) # URL에 접속
    time.sleep(3) # 웹 브라우저를 실행하고 URL에 접속할 때까지 기다림  
    
    if(scroll==True):
        # 수직(Y축 방향)으로 스크롤 동작하기 
        y = 0 # Y축 방향으로 스크롤 이동할 거리 초기화
        y_step = 1000
        for k in range(1, 5): # 반복 횟수 지정
            y = y + y_step  # 반복할 때마다 Y축 방향으로 더해지는 거리를 지정
            script = "window.scrollTo({0},{1})".format(0, y)
            driver.execute_script(script) # Y축 방향으로 스크롤
            time.sleep(3) # 결과를 받아올 때까지 잠시 기다림

    html = driver.page_source # 접속 후에 해당 page의 HTML 코드를 가져옴
    # driver.quit() # 웹 브라우저를 종료함
    
    soup = BeautifulSoup(html, 'lxml')
    
    # 동영상 제목과 URL 추출하기
    title_hrefs = soup.select('a#video-title')
    
    titles = []
    urls = []    
    for title_href in title_hrefs:
        title = title_href['title']         # 태그 안에서 title 속성의 값을 가져오기
        url = base_url + title_href['href'] # href 속성의 값 가져와 기본 url과 합치기        
        titles.append(title)
        urls.append(url)

    # 조회수와 업로드 시기 추출하기
    view_uploads = soup.select('span.style-scope.ytd-video-meta-block')
    
    view_numbers = view_uploads[0::2] # 인덱스가 짝수인 요소 선택
    upload_times = view_uploads[1::2] # 인덱스가 홀수인 요소 선택

    views = []
    uploads = [] 
    for view_number, upload_time in zip(view_numbers, upload_times):
        view = view_number.get_text().split(" ")[-1] # 조회수 추출
        upload = upload_time.get_text()              # 업로드 시기 추출
        views.append(view)
        uploads.append(upload)
        
    # 추출된 정보를 모으기
    search_results = []
    for title, url, view, upload in zip(titles, urls, views, uploads):
        search_result = [title, url, view, upload]
        search_results.append(search_result)
    
    # 추출 결과를 판다스 DataFrame 데이터 형식으로 변환
    df = pd.DataFrame(search_results, columns=["제목", "링크", "조회수", "업로드"])
    
    return df


# [7장: 331페이지]

# In[ ]:


df = get_data_from_youtube('방탄소년단') # get_data_from_youtube('방탄소년단', False) 도 가능
df.tail()
# df # 전체를 다 출력하려면 df.tail() 대신 df를 이용


# [7장: 333페이지]

# In[ ]:


df = get_data_from_youtube('방탄소년단', True)
df.tail() # 전체 중 끝 부분만 확인
# df # 전체를 다 출력하려면 df.tail() 대신 df를 이용


# ## 7.4 정리
