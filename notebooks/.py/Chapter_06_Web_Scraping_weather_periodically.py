# #### 날씨 정보 주기적으로 가져오기
# [6장: 245페이지]

# pip install schedule

import schedule
import time
from datetime import datetime

# 작업을 위한 함수 지정
def job():
    now = datetime.now()
    print("[작업 수행 시각] {:%H:%M:%S}".format(now))
    location = "경기도 수원시" # 날씨를 알고 싶은 지역 

    (txt_temp, txt_weather, wind_speed, humidity, pm10) = get_weather_daum(location)

    print("-------[오늘의 날씨 정보] (Daum) ----------")
    print(f"- 설정 지역: {location}")
    print(f"- 기온: {txt_temp}")
    print(f"- 날씨 정보: {txt_weather} ", )
    print(f"- 현재 풍속: {wind_speed}, 현재 습도: {humidity}, 미세 먼지: {pm10}")
    
    
# 작업 등록
# 코드 테스트를 위해 5초마다 날씨 정보 가져와 출력하기 위한 스케줄 설정
schedule.every(5).seconds.do(job)  # 5초(second)마다 job() 함수 실행 #웹서버에 부담을 안주려고

# -- 매일 지정한 시각에 날씨 정보를 가져와 출력하기 위한 스케줄 설정
# schedule.every().day.at("07:00").do(job) # 매일 07시에 job() 함수 실행
# schedule.every().day.at("12:00").do(job) # 매일 12시에 job() 함수 실행
# schedule.every().day.at("18:00").do(job) # 매일 18시에 job() 함수 실행
print("run pending...")

while True:
    try:
        schedule.run_pending() # 등록한작업 실행 및 기다림
        time.sleep(1)      # 1초 대기  # cpu 계속 잡아먹으니까 좀 줄이려고
    except:
        print("작업 강제 종료")
        schedule.clear()  # 기본 스케줄러 객체를 제거          
        break            # while 문을 빠져 나옴
        
#%%
while True:
    print("aaa")
    time.sleep(10)

#%%
import requests  
from bs4 import BeautifulSoup 
import time

def get_weather_daum(location):
    search_query = location + " 날씨"
    search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
    url = search_url + search_query
    html_weather = requests.get(url).text
    time.sleep(2)    
    soup_weather = BeautifulSoup(html_weather, "lxml")
    
    txt_temp = soup_weather.select_one('strong.txt_temp').get_text()  # 온도 
    txt_weather = soup_weather.select_one('span.txt_weather').get_text()  # 날씨 

    dl_weather_dds = soup_weather.select('dl.dl_weather dd')
    [wind_speed, humidity, pm10] = [x.get_text() for x in dl_weather_dds]  # 풍속 습도 미세먼지
    
    return (txt_temp, txt_weather, wind_speed, humidity, pm10, location)