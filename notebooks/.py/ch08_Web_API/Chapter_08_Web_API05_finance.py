#!/usr/bin/env python
# coding: utf-8

# [8장: 411페이지]
# ## 8.5 야후 파이낸스에서 주식 데이터 가져오기
# ### 8.5.1 설치 및 기본 사용법
# ### 8.5.2 미국 주식 데이터 가져오기

import yfinance as yf
# 실시간 주식정보를 가져오기는 힘들지만 지정한 기간동안 특정 주식종목의 데이터를 가지고오는 라이브러리
# 야후하이넨스의 공식 라이브러리가 아님

ticker_symbol = "TSLA" # 테슬라 주식 심볼
ticker_data = yf.Ticker(ticker_symbol)


# ticker_data.info  # 해당 종목의 정보 가져오기

# period 현재를 기준으로 가져올 데이터의 기간지정: 1d 5d 1m 3mo 6mo 1y 2y 5y 10y ytd max
# interval로 가지고올 데이터 간격 지정: 1m 2m 5m 15m 30m 60m 90m 1h 1d 5d 1wk 1mo 3mo
# start, end = 시작 종료일 지정(종료일은 포함x): 'YYYY-MM-DD'형식 end없으면 가장 최근까지
df = ticker_data.history(period='5d')  # history로 과거데이터 조회
df



# In[ ]:


df = ticker_data.history(period='1mo', interval='1d',start='2022-04-18', end='2022-04-22')
# period의 default는 1mo
df = ticker_data.history(start='2022-04-18', end='2022-04-23') # start와 end 모두 지정
# df = ticker_data.history(start='2022-04-18') # start만 지정하면 가장 최근까지 
df



# In[ ]:


# period는 대충 정하는거고 start end로 정확하게 지정됨 그래서 start end가 더썜
df_1mo = ticker_data.history(period='1mo')

df_start_end = ticker_data.history(period='1mo', interval='1d',start='2022-01-18', end='2022-06-22')
print(df_1mo.head(3)) # 2023-08-15 16 17로 시작
print(df_start_end.head(3))  # 2022-01-18 19 20로 시작


# In[ ]:

# datetime으로 날짜 지정할 수 있음
import datetime

start_p = datetime.datetime(2021,5,24) # 시작일 지정
end_p = datetime.datetime(2021,5,29)   # 종료일 지정

df = ticker_data.history(start=start_p, end=end_p) # start와 end 모두 지정
df




# In[ ]:
# ### 8.5.3 국내 주식 데이터 가져오기

# [8장: 414페이지]

import pandas as pd

#----------------------------------------------------
# 한국 주식의 종목 이름과 종목 코드를 가져오는 함수
#----------------------------------------------------
def get_stock_info(maket_type=None):
    # 한국거래소(KRX)에서 전체 상장법인 목록 가져오기
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"
    method = "download"
    if maket_type == 'kospi':
        marketType = "stockMkt"  # 주식 종목이 코스피인 경우
    elif maket_type == 'kosdaq':
        marketType = "kosdaqMkt" # 주식 종목이 코스닥인 경우
    elif maket_type == None:
        marketType = ""
    url = "{0}?method={1}&marketType={2}".format(base_url, method, marketType)

    df = pd.read_html(url, header=0, encoding='euc-kr')[0]  # excel파일이 리스트에 묶여서 한덩어리로 와서 [0]을 df로 넣음
    
    # 종목코드 열을 6자리 숫자로 표시된 문자열로 변환
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}") 
    
    # 회사명과 종목코드 열 데이터만 남김
    df = df[['회사명','종목코드']]
    
    return df


# [8장: 415페이지]

# In[ ]:

"""
----------------------------------------------------
  yfinance에 이용할 Ticker 심볼을 반환하는 함수
----------------------------------------------------
"""
def get_ticker_symbol(company_name, maket_type):

    df = get_stock_info(maket_type) # 함수로 정보를 받아옴
    code = df[df['회사명']==company_name]['종목코드'].values  # 코드를 꺼냄
    code = code[0]     # values가 array 안에 들어가있음 그걸 꺼내서 object로 바꿈 .values다시한다고 생각하면됨
    # array.Numpy -> '123456' 로 바꾸는거
    
    if maket_type == 'kospi':
        ticker_symbol = code +".KS" # 코스피 주식의 심볼 추가
    elif maket_type == 'kosdaq':
        ticker_symbol = code +".KQ" # 코스닥 주식의 심볼 추가
    
    return ticker_symbol


# In[ ]:


import yfinance as yf

ticker_symbol = get_ticker_symbol("삼성전자", "kospi") # 삼성전자, 주식 종류는 코스피로 지정
ticker_data = yf.Ticker(ticker_symbol)

df = ticker_data.history(start='2022-06-13', end='2022-06-18') # 시작일과 종료일 지정
# df = ticker_data.history(period='5d') # 기간을 지정



#%%
# 아래서 엑셀로 바꾸려니까 에러뜸
# ValueError: Excel does not support datetimes with timezones. Please ensure that datetimes are timezone unaware before writing to Excel.

# Date2라는 칼럼을 index의 형식을 바꿔서 만듬
df['Date2'] = df.index.strftime('%Y-%m-%d') 

# Date2를 인덱스로 설정
df.set_index(['Date2'], inplace=True)

# rename으로 인덱스 이름 다시 바꿈 
df.index.rename('Date', inplace = True)

# In[ ]:

# 가지고온 정보 엑셀로 저장
#  Excel does not support datetimes with timezones. 이라고 뜨면서 오류남 위에서 오류수정
excel_file_name = "../../../data/ch08/삼성전자_주가_데이터.xlsx" # 엑셀 파일 이름 지정
df.to_excel(excel_file_name)


print("생성 파일:", excel_file_name)




#%%

# [8장: 417페이지]
# ### 8.5.4 여러 주식 데이터 가져오기

# 하나의 주식 데이터 가지고오기
ticker_symbols = "MSFT" # 마이크로소프트 주식 심볼
# ticker_symbols = ["MSFT"] # 리스트도 지정해도 됨
df = yf.download(ticker_symbols, start="2020-01-01", end="2022-01-01")
df.tail()


#%%
# 그래프 그리기
import matplotlib.pyplot as plt

df['Close'].plot(grid=True, figsize=(15, 5), title="Microsoft")
plt.show()



# In[ ]:

# 여러 주식 데이터 가져오기
ticker_symbols = ["GOOG", "AAPL"] # 주식 심볼 리스트(구글, 애플)
df = yf.download(ticker_symbols,  start="2020-01-01", end="2022-01-01")
df.tail()
# 멀티인덱스 / 칼럼 형태로 저장됨
# df.columns()  하니까 안됨  # TypeError: 'MultiIndex' object is not callable

# In[ ]:


# 그래프 그리기
import matplotlib.pyplot as plt

df['Close'].plot(grid=True, figsize=(15, 5))
plt.show()


# [8장: 419페이지]

# In[ ]:


# 그래프 그리기
df['Close'].plot(grid=True, figsize=(15, 5), subplots=True, layout=(2,1))
plt.show()



