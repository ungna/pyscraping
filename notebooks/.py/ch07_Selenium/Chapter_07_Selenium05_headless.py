## 7장 셀레니움을 이용한 웹 스크레이핑


# [7장: 303페이지]

# ### 7.2.7 헤드리스(Headless) 웹 브라우저로 이미지 가지고오기
# 헤드리스: gui가 없는 웹브라우저 
# 처음에 할때는 gui가 있는것이 보기 편해서 좋기만 작동되면은 gui없이하는게 훨 빠름

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# 헤드레스로 하기위한 Options()으로 크롬작동
options = Options()                  # 옵션 설정을 위한 객체 생성
options.add_argument('headless')     # 헤드리스 웹 브라우저로 옵션 설정
# options.headless = True           # 이렇게도 가능
options.add_argument('window-size=1100,1000') # 웹 브라우저의 창 크기 설정

driver = Chrome(options=options)      # 옵션을 지정해 크롬 객체 생성

url = "https://finance.naver.com/"   # URL 지정
driver.get(url)                      # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)            # 웹 사이트의 내용을 받아오기까지 기다림

folder = "../../../data/ch07/"          # 폴더 지정
image_file = folder + "네이버_금융0913.png" # 생성할 이미지 파일 이름 지정
driver.save_screenshot(image_file)      # 웹 브라우저 내용을 캡처해 이미지 파일로 저장

driver.quit() # 웹 브라우저 종료

print("- 생성한 이미지 파일:", image_file) # 접속한 URL의 제목 출력