## 7장 셀레니움을 이용한 웹 스크레이핑
# requests는 자바스크립트가 포함된 동적 웹사이트에는 적용x
# 셀레니움은 가능


## 셀레니움으로 크롬 입장

from selenium.webdriver import Chrome

# 크롬 드라이버 객체 생성
# 셀레니움이 업데이트되서 드라이버 다운안해도되고 안넣어도됨
driver = Chrome()  
# driver = Chrome("C:/anaconda3/chromedriver.exe") # 크롬드라이버 넣은곳으로 path 설정 
driver.get("https://www.google.co.kr/")

# 웹 브라우저의 창 크기 설정
driver.set_window_size(800,600)
# driver.maximize_window()

print("- 접속한 웹사이트의 제목:", driver.title)   # 접속한 웹 사이트의 제목 출력
print(" -접속한 웹사이트의 URL:", driver.current_url)   # 접속한 웹 사이트의 URL 출력


#%%

# 구글에 입장해서 검색

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.google.co.kr/")

driver.maximize_window()

query = "python"
# 검색어를 입력할 수 있는 창의 이름을 찾음 # google은 ("name = q")  즉 By.NAME, "q"
input_element = driver.find_element(By.NAME, "q")   # By.속성, '입력값' 은 웹사이트마다 다름
input_element.send_key(query) # 검색창에 검색어 입력
input_element.submit()        # 검색결과 요청

print("- 접속한 웹 사이트의 제목:", driver.title) 
print("- 접속한 웹 사이트의 URL:", driver.current_url)


#%%

# 네이버에 입장해서 검색

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.google.co.kr/")

driver.maximize_window()

query = "python"
# 검색어를 입력할 수 있는 창을 찾음 # 네이버는 "query
input_element = driver.find_element(By.NAME, "query")
input_element.send_key(query) 
input_element.submit()        

print("- 접속한 웹 사이트의 제목:", driver.title) 
print("- 접속한 웹 사이트의 URL:", driver.current_url)



