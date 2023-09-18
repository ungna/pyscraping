## 7장 셀레니움을 이용한 웹 스크레이핑

# [7장: 300페이지]
# ### 7.2.6 웹 브라우저 내용을 이미지 파일로 저장


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

# 크롬에서 환율검색해서 들어가기
driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 780) # 웹 브라우저의 창 크기 설정

url = "https://www.google.com"   # URL 지정
driver.get(url)                  # 웹 브라우저를 실행해 지정한 URL에 접속

input_element = driver.find_element(By.NAME, "q") # 검색창 찾기
input_element.clear()                   # 검색창 내용 모두 지우기
query = "환율"
input_element.send_keys(query)         # 검색창에 검색어 입력
input_element.submit()                 # 검색 결과 요청


# 
folder = "../../../data/ch07/" # 폴더 지정
image_file = folder + "환율정보0913.png"  # 생성할 이미지 파일 이름 지정
driver.save_screenshot(image_file)    # 웹 브라우저 내용을 캡처해 이미지 파일로 저장

time.sleep(3) 
driver.quit()  # 웹 브라우저를 종료함

print("- 생성한 이미지 파일:", image_file) # 접속한 URL의 제목 출력

#%%
# 웹 브라우저로 이미지 파일 열기

driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 780) # 웹 브라우저의 창 크기 설정
# 상대경로로하니까 안되네;; rorkxdms
# driver.get(image_file)  # image_file = ../../../data/ch07/환율정보0913.png
driver.get("file:///D:/projAi_2023_ysh/books/pyscraping/data/ch07/환율정보0913.png")           # 웹 브라우저로 이미지 파일 열기



#%%%


# [7장: 303페이지]
# ### 7.2.7 헤드리스(Headless) 웹 브라우저로 이미지 가지고오기
# 헤드리스: gui가 없는 웹브라우저 
# 처음에 할때는 gui가 있는것이 보기 편해서 좋기만 작동되면은 gui없이하는게 훨 빠름

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

options = Options()                  # 옵션 설정을 위한 객체 생성
options.add_argument('headless')     # 헤드리스 웹 브라우저로 옵션 설정
options.add_argument('window-size=1100,1000') # 웹 브라우저의 창 크기 설정

# 옵션을 지정해 크롬 드라이버의 객체 생성
driver = Chrome(options=options)    

url = "https://finance.naver.com/"   # URL 지정
driver.get(url)                      # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)            # 웹 사이트의 내용을 받아오기까지 기다림

folder = "../../../data/ch07/"          # 폴더 지정
image_file = folder + "네이버_금융0913.png" # 생성할 이미지 파일 이름 지정
driver.save_screenshot(image_file)      # 웹 브라우저 내용을 캡처해 이미지 파일로 저장

driver.quit() # 웹 브라우저 종료

print("- 생성한 이미지 파일:", image_file) # 접속한 URL의 제목 출력