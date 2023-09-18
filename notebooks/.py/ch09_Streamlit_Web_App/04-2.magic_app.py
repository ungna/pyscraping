# magic 예제
# streamlit run 
# st.write랑 비슷함 
# " "안에 묶어두면 자동으로 st.write()가 적용되서 되는 원리

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

"# 스트림릿의 magic 명령어 사용 예"

"#### 텍스트 출력"
"일반 텍스트로 출력할 수도 있고, **마크다운**으로 출력할 수도 있습니다. :thumbsup:"

"#### 데이터 출력"
"숫자 데이터 출력:", 1234

df = pd.DataFrame({
        '1열': [10, 20, 30, 40],
        '2열': [50, 60, 70, 80,]})

"DataFrame 데이터 출력", df

# matplotlib을 이용한 그래프에 한글을 표시하기 위한 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 그래프를 위한 데이터 생성
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
df = pd.DataFrame(y, index=x)

# 그래프 그리기
ax = df.plot(grid=True, figsize=(15,4), legend=False)
ax.set_title("sin(x) 그래프", fontsize=20) # 그래프 제목을 지정
ax.set_xlabel("x", fontsize=15)            # x축 라벨을 지정
ax.set_ylabel("y", fontsize=15)            # y축 라벨을 지정
fig = ax.get_figure()                      # fig 객체 가져오기

"#### Matplotlib 차트 출력:", fig
