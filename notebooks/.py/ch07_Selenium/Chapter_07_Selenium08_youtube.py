## 7장 셀레니움을 이용한 웹 스크레이핑


#  유튜브 검색 결과 가져오기

# [7장: 324페이지]
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time

driver = Chrome() # 크롬 드라이버 객체 생성

base_url = "https://www.youtube.com" # 유튜브의 기본 URL
search_word =  '방탄소년단'          # 검색어
search_option = "&sp=CAMSAhAB"     # 조회수로 정렬
# 관련성:"&sp=CAASAhAB"  업로드날짜"&sp=CAISAhAB"  조회수:"&sp=CAMSAhAB"  평점:"&sp=CAESAhAB"

url = base_url +  '/results?search_query=' +  search_word  + search_option   # 접속하고자 하는 웹 사이트


driver.get(url) # 웹 브라우저를 실행해 지정한 URL에 접속
time.sleep(3)   # 웹 브라우저를 실행하고 URL에 접속할 때까지 기다림

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력


# 접속 후에 해당 page의 HTML 코드를 가져옴
html = driver.page_source 

driver.quit() # 웹 브라우저를 종료함


#%%

# 가지고온 HTML 파싱
soup = BeautifulSoup(html, 'lxml')
# selector을 선택해서 제목 뽑아냄  # select  vs select_one 이라서 
title_hrefs = soup.select('a#video-title')

title_hrefs[0] # 첫 번째 항목 출력
"""title_hrefs[0]
 <a id="video-title" class="yt-simple-endpoint style-scope ytd-video-renderer" title="BTS (방탄소년단) 'Dynamite' Official MV" aria-label="BTS (방탄소년단) 'Dynamite' Official MV 게시자: HYBE LABELS 조회수 1,739,327,245회 3년 전 3분 44초" href="/watch?v=gdZLi9oWNZg&amp;pp=ygUP67Cp7YOE7IaM64WE64uo">
            <yt-icon id="inline-title-icon" class="style-scope ytd-video-renderer" hidden=""><!--css-build:shady--><!--css-build:shady--></yt-icon>
            <yt-formatted-string class="style-scope ytd-video-renderer" aria-label="BTS (방탄소년단) 'Dynamite' Official MV 게시자: HYBE LABELS 조회수 1,739,327,245회 3년 전 3분 44초">BTS (방탄소년단) 'Dynamite' Official MV</yt-formatted-string>
          </a>
"""

title_hrefs[0].get('title') # title_hrefs[0]['title'] 도 동일

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


    
