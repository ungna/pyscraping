#!/usr/bin/env python
# coding: utf-8

# ## 8.3 RSS 피드 데이터 가져오기
# RSS: Really Simple Syndication / Rich Site Summary
# XML을 기초로 만들어진 데이터 형식으로 RSS 리더가 있으면 최신 RSS피드를 받아서 정보를 볼 수 있음

# ### 8.3.1 RSS 문서의 구조 및 데이터 추출

# [8장: 353페이지]

# RSS 샘플
rss_simple_document = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>파이썬 웹 스크레이핑 홈페이지</title>
  <link>https://www.python_web_scraping.com</link>
  <description>파이썬 웹 스크레이핑 설명</description>
  <pubDate>Sat, 30 Apr 2022 15:39:19 GMT</pubDate>
  <lastBuildDate>Sat, 30 Apr 2022 17:50:21 GMT</lastBuildDate>
  
  <item>
    <title>1장. 웹 스크레이핑</title>
    <link>https://www.python_web_scraping.com/web_scraping.html</link>
    <description>웹 스크레이핑 기본에 관한 교육</description>
    <pubDate>Sat, 30 Apr 2022 00:30:00 GMT</pubDate>
  </item>
  <item>
    <title>2장. 웹 API 교육</title>
    <link>https://www.python_web_scraping.com/web_api.html</link>
    <description>웹 API에 관한 교육</description>
    <pubDate>Sat, 30 Apr 2022 09:45:12 GMT</pubDate>
  </item>
</channel>

</rss>"""


# [8장: 355페이지]

# In[ ]:

# pip install feedparser
import feedparser
# RSS데이터를 dict형식으로 바로 변환하게 해주는 라이브러리

# RSS 형식의 데이터를 파싱
d = feedparser.parse(rss_simple_document) 

# 파싱 한것을 d.feed를 이용해 가지고 올 수 있음  # <channel> 에 있는 것들을 가지고옴
d.feed.title, d.feed.link, d.feed.description, d.feed.published, d.feed.updated


# In[ ]:


d["feed"]["title"], d["feed"]["link"], d["feed"]["description"], d["feed"]["published"], d["feed"]["updated"]


# [8장: 356페이지]

# In[ ]:

# d.entries를 이용해 <item>에 있는 것들을 가지고옴
d.entries[0].title, d.entries[0].link, d.entries[0].description, d.entries[0].published

d.entries[1].title, d.entries[1].link, d.entries[1].description, d.entries[1].published


# ### 8.3.2 구글 뉴스의 검색 기사 가져오기

# [8장: 358페이지]

# In[ ]:


import feedparser

query = "머신러닝"
# RSS 서비스 주소
rss_url = f'https://news.google.com/rss/search?q={query}&&hl=ko&gl=KR&ceid=KR:ko'
rss_news = feedparser.parse(rss_url) # RSS 형식의 데이터를 파싱

title = rss_news['feed']['title']
updated = rss_news['feed']['updated']

print("['구글 뉴스' RSS 피드 제목]", title)
print("['구글 뉴스' RSS 피드 제공 일시]", updated)


# In[ ]:
# 위에서 가지고온 updated가 Thu, 14 Sep 2023 04:58:51 GMT 이라서
# 한국시간으로 변경하는 함수를 만들어보자
    
from datetime import datetime, timedelta


# RSS 피드에서 받은 일시를 한국 날짜와 시간으로 변경
def get_local_datetime(rss_datetime):
    # 전체 값 중에서 날짜와 시간만 문자열로 추출
    date_time_str = ' '.join(rss_datetime.split()[1:5])
    
    # 문자열의 각 자리에 의미를 부여해 datetime 객체로 변경
    date_time_GMT = datetime.strptime(date_time_str, '%d %b %Y %H:%M:%S')
    
    # GMT에 9시간을 더해 한국 시간대로 변경
    date_time_KST = date_time_GMT + timedelta(hours=9)     
    
    return date_time_KST # 변경된 시간대의 날짜와 시각 반환

"""
datetime.strptime() 형식
연 월 일  : %Y %m %d   # %b 는 월(月)을 영어로 표시  ex Sep, Aug
시 분 초  : %H %M %S
"""

# In[ ]:

# 함수 적용
print("['구글 뉴스' RSS 피드 제공 일시]", get_local_datetime(updated))


# In[ ]:

# 뉴스내용 rss로 가지고오기
import feedparser
import pandas as pd

query = "머신러닝"
# RSS 서비스 주소
rss_url = f'https://news.google.com/rss/search?q={query}&&hl=ko&gl=KR&ceid=KR:ko'
rss_news = feedparser.parse(rss_url)

df_gnews = pd.DataFrame(rss_news.entries) # 구글 뉴스 아이템을 판다스 DataFrame으로 변환

selected_columns = ['title', 'published', 'link'] # 관심있는 열만 선택
df_gnews2 = df_gnews[selected_columns].copy()     # 선택한 열만 다른 DataFrame으로 복사

# published 열의 작성 일시를 한국 시간대로 변경
# df_gnews2['published'] 데이터를 꺼내서 apply()안의 함수 get_local_datetime에 apply함
df_gnews2['published'] = df_gnews2['published'].apply(get_local_datetime)  

df_gnews2.columns = ['제목', '제공 일시', '링크'] # 열 이름 변경
df_gnews2.head(3)                                 # 앞의 일부만 출력


# [8장: 360페이지]

# In[ ]:


from IPython.display import HTML

df = df_gnews2.head(3) # DataFrame 데이터의 일부 열과 행을 선택
# df = df_gnews2       # DataFrame 데이터 전체를 선택

html_table = df.to_html(escape=False, render_links=True) # DataFrame 데이터를 HTML 코드로 변환
HTML(html_table)  # HTML 코드의 내용을 웹 브라우저처럼 보여줌


# [8장: 361페이지]

# In[ ]:


from datetime import datetime, timedelta

google_news_datetime_KST = get_local_datetime(updated) # 한국 날짜와 시간으로 변경 

df = df_gnews2.head() # DataFrame 데이터 앞의 일부
# df = df_gnews2 # DataFrame 데이터 전체

# DataFrame 데이터를 HTML 코드로 변환 (justify='center' 옵션을 이용해 열 제목을 중간에 배치)
html_table = df.to_html(justify='center', escape=False, render_links=True) 

# HTML 기본 구조를 갖는 HTML 코드
html_code = '''
<!DOCTYPE html>
<html>
  <head>
    <title>구글 뉴스 검색</title>
  </head>
  <body>
    <h1>{0}</h1>
    <h3> *검색 날짜 및 시각: {1}</h3>
    {2}
  </body>
</html>    
'''.format(title, google_news_datetime_KST, html_table)

file_name = "C:/myPyScraping/data/ch08/google_news.html" # 생성할 HTML 파일 이름 지정
with open(file_name, 'w', encoding="utf-8") as f:
    f.write(html_code)
    
print("생성한 파일:", file_name)

