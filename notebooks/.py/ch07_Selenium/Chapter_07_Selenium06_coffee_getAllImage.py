## 7장 셀레니움을 이용한 웹 스크레이핑

# 스타벅스 이미지 전체 다운하기
# 함수만들기

from pathlib import Path
import requests


# 다운할 폴더 없으면 생성하는 함수
def makedir(download_folder):
    filepath = Path(download_folder)
    if not filepath.exists():
        filepath.mkdir(parents=True, exist_ok=True)  # parent = True면은 상위도 다 만들겠다는뜻 
        
# 뽑아온 이미지링크를 다운하는 함수
def download_img_from_link(url, image_path):  # (다운할 url, 다운받을 위치)
    req = requests.get(url)
    image_data = req.content # 응답 객체를 이용해 받은 이미지 데이터 
    with open(image_path, 'wb') as f:
        f.write(image_data)

# 폴더 만들기
download_folder = '../../../data/ch07/download/' 
makedir(download_folder)

#%%
# 스타벅스 이미지 전체 다운하기
# 홈페이지에서 이미지 url 뽑아오고 for문으로 다운하기

# 이미지 url 뽑아오기
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

driver.quit()  

# for문으로 다운하기
for drink_product in drink_products:  # for문으로 하나씩 가지고옴
    menu_name = drink_product.select_one('dd').get_text()  # select_one을 써야지 .get_text()가 먹힘
    menu_photo_link = drink_product.select_one('a img')['src']
    print(menu_name, menu_photo_link)
    
    image_path = download_folder + menu_name + ".png"  # 다운할 위치를 image_path로 저장
    download_img_from_link(menu_photo_link, image_path)
    
    
