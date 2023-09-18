import requests  
from bs4 import BeautifulSoup 

url = "https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=H_C_1_1"

html_lotto = requests.get(url).text  # request해서 결과를 받아옴
soup_lotto = BeautifulSoup(html_lotto, "lxml")  # 받아온거를 파싱함
print(url)

txt_temp = soup_lotto.select('span.ball_645') 
txt_temp

[x.get_text() for x in soup_lotto.select('span.ball_645')]

#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball1
#%%
import requests  
from bs4 import BeautifulSoup 

url = "https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=H_C_1_1"

html_lotto = requests.get(url).text  # request해서 결과를 받아옴
soup_lotto = BeautifulSoup(html_lotto, "lxml")  # 받아온거를 파싱함
print(url)

txt_list = soup_lotto.select('select#dwrNoList') # 텍스트만 저장
txt_list

[x.get_text() for x in soup_lotto.select('select#dwrNoList')]
# 문제점: 회차별로 url이 달라서 회차별로 못 뽑았음

