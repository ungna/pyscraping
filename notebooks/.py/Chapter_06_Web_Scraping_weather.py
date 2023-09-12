
import requests  
from bs4 import BeautifulSoup 

location = "서울시 종로구 청운동"
search_query = location + " 날씨"
search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
url = search_url + search_query

html_weather = requests.get(url).text  # request해서 결과를 받아옴
soup_weather = BeautifulSoup(html_weather, "lxml")  # 받아온거를 파싱함
print(url)

#%%
txt_temp = soup_weather.select_one('strong.txt_temp').get_text()  # 텍스트만 저장
txt_temp

#%%

txt_weather = soup_weather.select_one('span.txt_weather').get_text()
txt_weather

#%%

dl_weather_dds = soup_weather.select('dl.dl_weather dd')
dl_weather_dds

#%%

[wind_speed, humidity, pm10] = [x.get_text() for x in dl_weather_dds]
# 위에꺼 언패킹
# dl_weather_dds_text = [x.get_text() for x in dl_weather_dds]
# [wind_speed, humidity, pm10] = dl_weather_dds_text

print(f"현재 풍속: {wind_speed}, 현재 습도: {humidity}, 미세 먼지: {pm10}")
print("현재 풍속: {}, 현재 습도: {}, 미세먼지: {}".format(wind_speed, humidity, pm10))

#%%
# 위에서 한거 다 합쳐서 함수화

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


# In[ ]:
# 함수 사용1

location = "서울시 종로구 청운동" # 날씨를 알고 싶은 지역 
get_weather_daum(location)        # 함수 호출


#%%
# 함수사용2

location = "경기도 수원시" # 날씨를 알고 싶은 지역 

(txt_temp, txt_weather, wind_speed, humidity, pm10) = get_weather_daum(location)
print("-------[오늘의 날씨 정보] (Daum) ----------")
print(f"- 설정 지역: {location}")
print(f"- 기온: {txt_temp}")
print(f"- 날씨 정보: {txt_weather} ", )
print(f"- 현재 풍속: {wind_speed}, 현재 습도: {humidity}, 미세 먼지: {pm10}")

#%%

# 안됨
# https://digiconfactory.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%AC%EB%A1%A4%EB%A7%81-%EA%B8%B0%EC%83%81%EC%B2%AD-%ED%98%84%EC%9E%AC-%EB%82%A0%EC%94%A8-%EC%A0%95%EB%B3%B4-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0
import requests  
from bs4 import BeautifulSoup 

url = "https://www.weather.go.kr/w/obs-climate/land/city-obs.do?auto_man=m&stn=0&dtm=&type=t99&reg=109&tm=2023.09.12.11%3A00"

html_weather = requests.get(url).text  # request해서 결과를 받아옴
soup_weather = BeautifulSoup(html_weather, "lxml")  # 받아온거를 파싱함

table = soup_weather.find('table#weather_table.tr.a')

            

