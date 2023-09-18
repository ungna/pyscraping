# 데이터 표시 예제2
# streamlit run 02.data_app2.py
# 데이터 표소하는 요소 크게 4가지가 있음
"""
1. st.dataframe(df_data):  상호작용 가능
2. st.table(df_data):  상호작용 불가능
3. st.metric(label, value): 라벨과 값(온도, 습도 등) 표시
4. st.json(json_data): JSON 데이터 표시
"""

# st.json  st.metric
import streamlit as st
import pandas as pd
import json

# 딕셔너리 데이터
dict_data = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "신체정보": {
        "키": 175.4,
        "몸무게": 71.2
    },
    "취미": [
        "등산",
        "자전거타기",
        "독서"
    ]
}

# 딕셔너리 데이터를 JSON 데이터로 변경
json_data = json.dumps(dict_data, indent=3, sort_keys=True, ensure_ascii=False)

st.title("스트림릿에서 데이터 표시 (2/2)")

st.subheader("st.json() 이용")
st.json(json_data)

st.subheader("st.metric() 이용")
st.metric("온도", "25 °C", delta="1.5 °C")
