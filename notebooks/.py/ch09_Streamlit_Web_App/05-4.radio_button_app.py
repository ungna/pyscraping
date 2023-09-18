# 라디오 버튼 사용 예제
# streamlit run 

import streamlit as st
import pandas as pd

st.title("스트림릿의 라디오 버튼 사용 예")

radio1_options = ['10', '20', '30', '40']
radio1_selected = st.radio('1. (5 x 5 + 5)은 얼마인가요?', radio1_options)
# st.radio('문구', radio_option, radio_option)
st.write('**선택한 답**:', radio1_selected)
        
radio2_options = ['마라톤', '축구', '수영', '승마']
# index=0  을 넣으면 원하는 위치에 default값이 설정됨
radio2_selected = st.radio('2. 당신이 좋아하는 운동은?', radio2_options, index=2)  # index=2는 radio2_options[2]라는 뜻
st.write('**당신의 선택**:', radio2_selected)
