## 7장 셀레니움을 이용한 웹 스크레이핑

# [7장: 299페이지]
### 웹 브라우저 스크롤

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

# 검색하기
driver = Chrome()                  # 크롬 드라이버 객체 생성
driver.set_window_size(1000, 1000) # 웹 브라우저의 창 크기 설정

url = "https://www.google.com"     # URL 지정
driver.get(url)                    # 웹 브라우저를 실행해 지정한 URL에 접속

input_element = driver.find_element(By.NAME, "q") # 검색창 찾기
input_element.clear()              # 검색창 내용 모두 지우기
query = "python"
input_element.send_keys(query)     # 검색창에 검색어 입력
input_element.submit()             # 검색 결과 요청


# 스크롤해서 밑으로 내리기
# 웹 사이트 문서 높이 가져오기
scroll_height = driver.execute_script("return document.body.scrollHeight")
print("- 웹 사이트 문서 높이:", scroll_height)

y = 0         # Y축 좌표의 초깃값
y_step = 200  # Y축 아래로 이동하는 단계

while (True):
    y = y + y_step
    script =  "window.scrollTo(0,{0})".format(y) 
    # driver.execute_script("window.scrollTo(0,y))  # 절대위치로 수직 스크롤  # y대신에 dy넣으면 상대위치
    driver.execute_script(script)   # 스크립트 실행 # y+y_step만큼 이동(200)
    time.sleep(1)                   # 데이터를 받아올 때까지 기다림
    
    # 수식 스크롤 위치가 문서 끝보다 크거나 같으면 while 문 빠져나가기
    if (y >= scroll_height):
        break
    

