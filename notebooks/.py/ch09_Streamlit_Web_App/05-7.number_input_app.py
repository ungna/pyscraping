# 숫자 입력의 사용 예제
# number_input
# streamlit run 

import streamlit as st

st.title("스트림릿의 숫자 입력 사용 예")

# number_input가 숫자 입력하는거라 그런지 +-버튼으로 하나씩 올리게 하는거 있음
# value: 기본적으로 처음 보이는 default값 value를 지정안하면은 min_value이 들어감
number1 = st.number_input('20 이상의 두 자리 숫자를 입력하세요', min_value=20, max_value=99)
st.write('**입력한 숫자**', number1)

height = st.number_input('키(cm)를 입력하세요', min_value=1.0, value=170.0, step=0.1) # step: +-버튼으로 올리는 숫자 조정
weight = st.number_input('몸무게(kg)를 입력하세요', min_value=1.0, value=65.5)
BMI = weight/((height/100)**2)
st.write('**신체질량지수(BMI):**', BMI )
