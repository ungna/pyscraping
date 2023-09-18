#!/usr/bin/env python
# coding: utf-8

# ## 8.2 API 키 없이 시간 관련 데이터 가져오기 
# ### 8.2.1 시간대 리스트와 현재 시각 데이터 가져오기

import requests  
import json

# 가지고올 수 있는 모든 시간대 가져오기
url = "https://timeapi.io/api/TimeZone/AvailableTimeZones"  

r = requests.get(url)
r.text[:70] # 문자열 중 앞의 일부만 출력
# r.text    # 문자열 전체를 출력
rt = r.text   # type 이 str로 전체가 하나의 str로 되있음 # r.text[1] 하면은 A 가나옴


# In[ ]:
# [8장: 346페이지]

import requests  
import json

# 서울의 시간 받아오기
# url에 ?timeZone=Asia/Seoul 을 추가해서 서울의 시간 받아옴
url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Seoul"

r = requests.get(url)
print(r.text)   # 리턴된 값이 JSON형태


#%%

# url과 매개변수를 분리해서 따로 요청해서 받아옴
url = "https://timeapi.io/api/Time/current/zone" # 요청 주소
parameters = {"timeZone": "Asia/Seoul"}          # 요청 매개 변수 생성

# request할때 "timeZone": "Asia/Seoul" 인 것을 받아옴
r = requests.get(url, params=parameters)
print(r.text) 

print(type(r))  # 리턴된 값이 JSON형태


# dict로 변환
json_to_dict = json.loads(r.text)
type(json_to_dict)  # dict



# In[ ]:
    
# 지금까지는 웹API의 응답(r)을 r.text로 가지고 온다음에 
# json_to_dict = json.loads(r.text) 이렇게 2단계를 거쳐서 dict으로 바꿈

# 한방에 JSON 형태의 데이터를 파이썬의 딕셔너리 타입으로 변환
json_to_dict = r.json()
type(json_to_dict)


# In[ ]:

# 서울 시간대를 받아오는것을 간단하게 dict로 변환하는거 요약

import requests
import json

url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Seoul"

date_time_dict = requests.get(url).json()
print(f"타입: {type(date_time_dict)} 내용: {date_time_dict}")


# [8장: 348페이지]

# In[ ]:

# dict형식으로 바꾼 다음 원하는 키의 값을 뽑아내기
date_time_dict["dateTime"], date_time_dict["timeZone"], date_time_dict["dayOfWeek"]



# In[ ]:
    ##################에러 안됨
# [8장: 349페이지]
# ### 8.2.2 시간대 변환 데이터 가져오기
# POST로 해보기

import requests
import json

url = 'https://timeapi.io/api/Conversion/ConvertTimeZone' # 요청 주소

from_time_zone = "Asia/Seoul"
from_date_time = "2023-09-14 10:00:00"
to_time_zone = "UTC" # GMT로 지정해도 결과는 동일

headers = {"Content-Type": "application/json"}

# json형태로 변경
json_data = json.dumps({"fromTimeZone": from_time_zone,
                        "dateTime": from_date_time,
                        "toTimeZone": to_time_zone})


# POST 방법으로 요청해 응답받음
r = requests.post(url, headers=headers, data=json_data) 


# 받아온걸 dict로 바꿈 # 여기서 에러남 header에서 먼가 누락된게 있는거같음
ctz_json_to_dict = r.json()
ctz_json_to_dict


# In[ ]:
    
# [8장: 349페이지]
# ### 8.2.2 시간대 변환 데이터 가져오기
# GET로 해보기

import requests
import json

url = 'https://timeapi.io/api/Conversion/ConvertTimeZone' # 요청 주소

from_time_zone = "Asia/Seoul"
from_date_time = "2023-09-14 10:00:00"
to_time_zone = "UTC" # GMT로 지정해도 결과는 동일

headers = {"Content-Type": "application/json"}

# dict형태로 변경
dict_data = {"fromTimeZone": from_time_zone,
                        "dateTime": from_date_time,
                        "toTimeZone": to_time_zone}


# GET 방식으로 요청  형식이 좀 다름  # params에 dict형식이 와야됨
r = requests.get(url, params = dict_data) 

# 받아온걸 dict로 바꿈 # 여기서 에러남 받아온게 r이 좀 이상한듯
ctz_json_to_dict = r.json()
ctz_json_to_dict
# [8장: 350페이지]

# In[ ]:


import requests
import json

url = 'https://timeapi.io/api/Conversion/ConvertTimeZone' # 요청 주소

from_time_zone = "Asia/Seoul"
from_date_time = "2022-10-03 10:03:00"
to_time_zone = "GMT" # UTC로 지정해도 결과는 동일

dict_data = {"fromTimeZone": from_time_zone,
              "dateTime": from_date_time,
              "toTimeZone": to_time_zone}

r = requests.post(url, json=dict_data) # POST 방법으로 요청해 응답받음
ctz_json_to_dict = r.json()
ctz_json_to_dict


# [8장: 351페이지]

# In[ ]:


dateTime = ctz_json_to_dict['conversionResult']['dateTime'] # 변환된 날짜와 시각 데이터를 추출
to_date_time = f"{dateTime.split('T')[0]} {dateTime.split('T')[1]}"
from_date_time, to_date_time

