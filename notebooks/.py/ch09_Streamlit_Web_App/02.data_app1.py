# 데이터 표시 예제1
# streamlit run 02.data_app1.py
# 데이터 표소하는 요소 크게 4가지가 있음
"""
1. st.dataframe(df_data):  상호작용 가능
2. st.table(df_data):  상호작용 불가능
3. st.metric(label, value): 라벨과 값(온도, 습도 등) 표시
4. st.json(json_data): JSON 데이터 표시
"""

# dataframe, table
import streamlit as st
import pandas as pd

# CSV 파일 경로
# folder = '../../../data/ch09/' # 폴더 경로를 지정 # 상대경로 안되나 ㅠ
folder = 'D:/projAi_2023_ysh/books/pyscraping/data/ch09/'  # 폴더 경로를 지정
csv_file = folder + 'korea_rain1.csv' # 파일 경로를 지정

# CSV 파일을 읽어와서 DataFrame 데이터 생성
df = pd.read_csv(csv_file, encoding="utf-8")

st.title("스트림릿에서 데이터 표시 (1/2)")

st.subheader("st.dataframe() 이용")
st.dataframe(df)

st.subheader("st.table() 이용")
st.table(df)
