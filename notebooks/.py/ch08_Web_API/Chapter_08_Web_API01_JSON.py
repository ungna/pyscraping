#!/usr/bin/env python
# coding: utf-8

# # 8장 웹 API
# API(application programming interface):  일종의 소프트웨어 인터페이스이며 다른 종류의 소프트웨어에 서비스를 제공한다
# API의 한 가지 목적은 시스템이 동작하는 방식에 관한 내부의 세세한 부분을 숨기는 것으로,
# 내부의 세세한 부분이 나중에 변경되더라도 프로그래머가 유용하게 사용할 수 있고 일정하게 관리할 수 있는 부분들만 노출시킨다
 
# ## 8.1 웹 API의 이해
# 웹 API: API라는 용어는 웹 API를 의미하기도 하며, 이는 인터넷에 의해 병합된 컴퓨터들 간 통신을 허용한다

# ### 8.1.1 웹 API의 데이터 획득 과정

# ### 8.1.2 웹 API의 인증 방식

# ### 8.1.3 응답 데이터의 형식 및 처리

# #### JSON 데이터 형식

# #### JSON 데이터 변환 및 데이터 추출

# [8장: 341페이지]

# In[ ]:
# JSON 데이터 형식
# JSON은 자바스크립트와 함께 사용될 목적으로 만들었지만 대부분의 언어에 이용할 수 있다
# dict과 구조가 비슷함

import json

python_dict = {
    "이름": "홍길동",  # 문자열은 ""로 감쌈
    "나이": 25,
    "거주지": "서울",
    "신체정보": {  # 객체는 중괄호로 감쌈
        "키": 175.4,
        "몸무게": 71.2
    },
    "취미": [  # 배열은 대괄호로 감쌈
        "등산",
        "자전거타기",
        "독서"
    ]
}

print("python_dict type: ",type(python_dict))  # dict


# json 형태의 데이터로 변경 
json_data = json.dumps(python_dict)
print("json_data type: ",type(json_data))  # str


#%%
# [8장: 342페이지]

# JSON파일 이랑 dict 비교해보기
print("\n python_dict: \n",python_dict)

print("json_data: \n",json_data)


# In[ ]:
# # json 형태의 데이터로 변경하는데 옵션을 줘서 알아보기 쉽게하기

# indent: 들여쓰기
# sort_keys: 키정렬여부
# ensure_ascii: ascii형식으로 변환x
json_data = json.dumps(python_dict, indent=3, sort_keys=True, ensure_ascii=False)
print(json_data)


#%%

# JSON 데이터를 다시 파이썬의 딕셔너리 타입으로 변환
dict_data = json.loads(json_data) 
type(dict_data)


# In[ ]:

# dict에서 정보빼내기
dict_data['신체정보']['몸무게']

dict_data['취미']

dict_data['취미'][0]



