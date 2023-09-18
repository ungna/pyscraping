# 기본 버튼 입력 예제
# streamlit run 

import streamlit as st

# 버튼을 클릭하면은 이벤트 적용하는게 일반적인데
# 여기서는 다시 코드를 실행해서 if else함수로 이벤트를 구현?함
# 버튼 클릭하면은 모듈이 다시 실행되서 다시 위에서부터 적용 그리고 그떄 클릭한 버튼만 true가 됨
st.title("스트림릿의 버튼 입력 사용 예")

clicked = st.button('버튼 1')  # 버튼이 생성됨  
# st.button('버튼 1')만 있어도 생성됨
st.write('버튼 1 클릭 상태:', clicked)  # clicked: 현상태(클릭됬는지 안됬는지) 를 True False로 보여줌

if clicked:  # 여기 clicked는 버튼 1에 영향을 받음
     st.write('버튼 1을 클릭했습니다.' )
else:
     st.write('버튼 1을 클릭하지 않았습니다.' )
  
# 여기에 하나 더 넣어도 버튼 1 영향 아래에 있음
if clicked:  # 여기 clicked는 버튼 1에 영향을 받음
     st.write('버튼 2를 클릭했습니다.' )
else:
     st.write('버튼 2를 클릭하지 않았습니다.' )
      

clicked = st.button('버튼 2')
st.write('버튼 2 클릭 상태:', clicked)

if clicked:  # 여기 clicked는 버튼 2에 영향을 받음
     st.write('버튼 2를 클릭했습니다.' )
else:
     st.write('버튼 2를 클릭하지 않았습니다.' )


clicked = st.button('버튼 3')
st.write('버튼 3 클릭 상태:', clicked)

if clicked:  # 여기 clicked는 버튼 2에 영향을 받음
     st.write('버튼 3를 클릭했습니다.' )
else:
     st.write('버튼 3를 클릭하지 않았습니다.' )