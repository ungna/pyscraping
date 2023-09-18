## 7장 셀레니움을 이용한 웹 스크레이핑

# 비트코인 거래정보 가지고오기
# [7장: 317페이지]

# requests로 받아오기
import requests
import pandas as pd

url = "http://coinmarketcap.com/ko/" # URL 지정
html = requests.get(url).text        # HTML 소스 가져오기
dfs = pd.read_html(html)             # HTML 소스에서 table의 내용을 DataFrame 리스트로 변환

df = dfs[0]       # 리스트의 첫 번째 요소를 선택
df.iloc[0:12,1:6] # DataFrame 데이터에서 행과 열을 선택해 출력

# 문제: 위에 10개만 나오고 밑에는 안나옴

#%%

# seleniumm 사용

from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

driver = Chrome()          # 크롬 드라이버 객체 생성

url = "https://coinmarketcap.com/ko/" # URL 지정
driver.get(url)            # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)  # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source  # 접속 후에 해당 page의 HTML 소스를 가져옴
dfs = pd.read_html(html)   # HTML 소스에서 table의 내용을 DataFrame 리스트로 변환

driver.quit()  # 웹 브라우저 닫기

df = dfs[0]       # 리스트의 첫 번째 요소를 선택
df.iloc[0:16,1:6] # DataFrame 데이터에서 행과 열을 선택해 출력

# 수직 스크롤으로 이동해야 서버가 데이터를 가져옴으로 스크롤 기능을 넣어야됨

#%%
# [7장: 319페이지]
# 수직스크롤 기능 추가


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

driver.quit()  # 웹 브라우저 닫기

df = dfs[0]         # 리스트의 첫 번째 요소를 선택

 # DataFrame 데이터에서 행과 열을 선택해 출력
df.iloc[95:100,1:6]  # 아래 95~100번째 index , 칼럼 1:6

df.iloc[0:5,1:6]


# In[ ]:

# 예전에는 이름에 Bitcoin1BTC구매하기  이런식으로 되있어서 깔끔하게 제거용
df['이름'] = [name.replace(str(num), " ") for num, name in zip(df['#'], df['이름'])]
df['이름'] = [name.replace("구매하기", "") for name in df['이름']]
df.iloc[0:5,1:6]



#%%
# [7장: 321페이지]
# 1페이지당 100개씩만 있어서 페이지 번호 지정하면 그 페이지읽는 함수만들기

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

    df = dfs[0] # 리스트의 첫 번째 요소를 선택해서 
    
    
    driver.quit() # 웹 브라우저를 종료함

    return df.iloc[:,1:9]


# [7장: 322페이지]

# In[ ]:
# 2페이지 지정해서 함수실행해보기
from IPython.display import display

page_num = 2 # page 지정
df_coin = get_coin_info(page_num) # 함수 호출

# DataFrame 데이터에서 행과 열을 선택해 display로 출력 
with pd.option_context('display.max_rows',2):
    pd.set_option("show_dimensions", False) # DataFrame의 행과 열 개수 출력 안 하기
    display(df_coin.iloc[:,0:6])


    
