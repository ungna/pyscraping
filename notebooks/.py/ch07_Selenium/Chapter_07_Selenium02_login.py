## 7장 셀레니움을 이용한 웹 스크레이핑

# [7장: 295페이지]
## 카카오 계정으로 로그인해보기

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
user_id = driver.find_element(By.NAME, "loginId")         # name 속성으로 아이디(ID) 입력창 찾기
user_id.send_keys(my_id)                                # 아이디 전송

# 패스워드 입력
# user_pw = driver.find_element(By.ID, "id_password_3") # id 속성으로 패스워드(비밀번호) 입력창 찾기 
user_pw = driver.find_element(By.NAME, "password")      # name 속성으로 패스워드(비밀번호) 입력창 찾기
user_pw.send_keys(my_pw)                                # 패스워드 전송
time.sleep(1)

# 로그인 버튼 클릭하기 
xpath = '//*[@id="mainContent"]/div/div/form/div[4]/button[1]' # 우클릭하고 copy > copyXPath
login_button = driver.find_element(By.XPATH, xpath)       # XPath로 로그인 버튼 찾기
login_button.click()                                      # 버튼 클릭
    
print("- 접속한 웹 사이트의 제목:", driver.title)       # 접속한 URL의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url)  # 접속한 URL 출력


#%%

# 네이버 로그인해보기
# 네이버는 위같이하면은 자동입력방지문자를 입력하라는 사이트로 넘어감

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()                # 크롬 드라이버 객체 생성
driver.set_window_size(800, 900) # 웹 브라우저의 창 크기 설정

url = "https://nid.naver.com/"   # 네이버 계정 로그인 URL 지정
driver.get(url)                  # 웹 브라우저를 실행해 지정한 URL에 접속

my_id = "naver_id"               # 자신의 아이디 입력
my_pw = "naver_password"         # 자신의 패스워드 입력

# 자바스크립트로 입력해야함
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
