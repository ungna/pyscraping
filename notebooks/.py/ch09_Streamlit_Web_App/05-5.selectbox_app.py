# 셀렉트박스 사용 예제
# streamlit run 
# radio랑 형식은 똑같음

import streamlit as st

st.title("스트림릿의 셀렉트박스 사용 예")

selectbox1_options = ['하이든', '모짜르트', '베토벤', '슈만']
your_option1 = st.selectbox('1. 좋아하는 음악가는?', selectbox1_options)
st.write('**당신의 선택**:', your_option1)

selectbox2_options = ['보티첼리', '램브란트', '피카소', '뭉크']
your_option2 = st.selectbox('2. 좋아하는 화가는?', selectbox2_options)
st.write('**당신의 선택**:', your_option2)
