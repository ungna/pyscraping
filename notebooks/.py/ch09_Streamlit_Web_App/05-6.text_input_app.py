# 텍스트 입력의 사용 예제 
# st.text_input으로 사용자가 텍스트를 입력할 수 있음
# streamlit run 

import streamlit as st

st.title("스트림릿의 텍스트 입력 사용 예")

# value = 기본적으로 입력되있는 값
user_id = st.text_input('아이디(ID) 입력', value="streamlit", max_chars=15) # max_chars = 길이제한
user_password = st.text_input('패스워드(Password) 입력', value="abcd", type="password") # type="password" 입력한걸 *로표시
                                                                                        # 안보이는거 보이게 클릭하느것도 있음

if user_id == "streamlit":
    if user_password == "1234":
        st.write('로그인 됐습니다. 서비스를 이용할 수 있습니다.')
    else:
        st.write('잘못된 패스워드입니다. 다시 입력하세요.')
else:
    st.write('없는 ID 입니다. 회원 가입을 하거나 올바른 ID를 입력하세요.')
