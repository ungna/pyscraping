#!/usr/bin/env python
# coding: utf-8

# ## 8.4 스포티파이를 이용한 노래 데이터 가져오기

# ### 8.4.1 앱 만들고 액세스 토큰 생성

# #### 개발자 웹 사이트에서 앱 만들기

# #### 액세스 토큰 생성

# [8장: 368페이지]

# In[ ]:


import requests

## 자신의 Client ID와 Client Secret 입력
# CLIENT_ID = '5df50a2c54ab3b1987b03bd42af2ac09'
# CLIENT_SECRET = '81ca98ebh0b74231b9c2c06269e9647d'

url = 'https://accounts.spotify.com/api/token'

auth_data = {'grant_type': 'client_credentials',
              'client_id': CLIENT_ID,
              'client_secret': CLIENT_SECRET}

r = requests.post(url, data=auth_data) # POST 방법으로 응답을 요청
r_token = r.json() # 응답 객체의 JSON 형식의 데이터를 딕셔너리 타입으로 변환
r_token


# In[ ]:


def get_spotify_access_token(client_id, client_secret):
    
    url = 'https://accounts.spotify.com/api/token'

    auth_data = {'grant_type': 'client_credentials',
                  'client_id': client_id,
                  'client_secret': client_secret}
        
    r = requests.post(url, data=auth_data) # POST 방법으로 응답을 요청
    r_token = r.json() # 응답 객체의 text 부분을 JSON 형식으로 변환
    
    return r_token['access_token']


# [8장: 369페이지]

# In[ ]:


ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)
ACCESS_TOKEN


# ### 8.4.2 아티스트 API로 아티스트 관련 정보 가져오기

# #### 아티스트 정보 가져오기

# [8장: 374페이지]

# In[ ]:


import requests

def get_spotify_artist_info(artist_id):
    url = "https://api.spotify.com/v1/artists/{id}".format(id=artist_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)
    headers = {"Authorization": "Bearer " + ACCESS_TOKEN}

    r = requests.get(url, headers=headers)

    return r.json()


# [8장: 375페이지]

# In[ ]:


artist_id = "3HqSLMAZ3g3d5poNaI7GOU" # 아이유의 아티스트 ID
artist_data = get_spotify_artist_info(artist_id)

print("[아티스트 관련 정보]")
print("- 이름:", artist_data['name'])
print("- ID:", artist_data['id'])
print("- 장르:", artist_data['genres'])
print("- 인기도:", artist_data['popularity'])


# In[ ]:


artist_id = "3Nrfpe0tUJi4K4DXYWgMUX" # 방탄소년단(BTS)의 아티스트 ID
artist_data = get_spotify_artist_info(artist_id)

print("[아티스트 관련 정보]")
print("- 이름:", artist_data['name'])
print("- ID:", artist_data['id'])
print("- 장르:", artist_data['genres'])
print("- 인기도:", artist_data['popularity'])


# #### 아티스트의 인기곡 정보 가져오기

# [8장: 379페이지]

# In[ ]:


url = "https://api.spotify.com/v1/markets"

ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)
headers = {"Authorization": "Bearer " + ACCESS_TOKEN}

r = requests.get(url, headers=headers)
r.text[:50] # 앞의 일부만 표시
# r.text     # 전체 표시


# In[ ]:


def get_spotify_artist_top_tracks(artist_id, country_code):

    url = "https://api.spotify.com/v1/artists/{id}/top-tracks".format(id=artist_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)
    headers = {"Authorization": "Bearer " + ACCESS_TOKEN}
    parameters = {"market": country_code}
    r = requests.get(url, params=parameters, headers=headers)

    return r.json()


# [8장: 380페이지]

# In[ ]:


import pandas as pd

artist_id = "3HqSLMAZ3g3d5poNaI7GOU" # 아이유의 아티스트 ID
country_code = "KR" # 대한민국의 국가 코드

# 인기곡 정보 JSON 객체 받기
artist_top_tracks_data = get_spotify_artist_top_tracks(artist_id, country_code)
# 인기곡 정보 JSON 데이터에서 곡 정보 객체 리스트 추출
top_tracks = artist_top_tracks_data['tracks']

[type(top_tracks), len(top_tracks)] # top_tracks의 타입과 개수 출력


# In[ ]:


top_tracks[0].keys() # 리스트의 첫 번째 요소로 있는 딕셔너리에서 키만 추출


# In[ ]:


# 리스트를 DataFrame 데이터로 변환
df_artist_top_track = pd.DataFrame(top_tracks)
# DataFrame 데이터에서 열 선택
df_artist_top_track2 = df_artist_top_track[['artists', 'name', 'duration_ms', 'id', 'popularity']]

df_artist_top_track2.head()


# [8장: 381페이지]

# In[ ]:


def get_artists(artists_info):
    artists_name = []
    for artist_info in artists_info:
        name = artist_info['name'] # 아티스트 정보 중 이름만 추출
        artists_name.append(name)  # 아티스트 이름을 리스트로 묶음
    
    artists_name_str = ", ".join(artists_name) # 리스트로 된 아티스트 이름을 문자열로 변환 
    return artists_name_str


# In[ ]:


df_artist_top_track3 = df_artist_top_track2.copy() # DataFrame 데이터 복사

# get_artists() 함수를 artists 열의 각 항목에 적용
df_artist_top_track3['artists'] = df_artist_top_track3['artists'].apply(get_artists)
df_artist_top_track3.head()


# In[ ]:


def convert_msec(msec):
    milliseconds = (msec%1000)
    seconds = (msec/1000) % 60
    seconds = int(seconds)
    minutes = (msec/(1000*60)) % 60
    # minutes = (msec/1000) // 60  # 이렇게 해도됨
    minutes = int(minutes)
    hours = (msec/(1000*60*60)) % 60
    hours = int(hours)
    
    hms_str = "{0:02d}:{1:02d}:{2:02d}.{3:03d}".format(hours, minutes, seconds, milliseconds)
    return hms_str

#%%
convert_msec(214253)

# [8장: 383페이지]

# In[ ]:


df_IU_top_track = df_artist_top_track3.copy() # DataFrame 데이터 복사

# convert_msec() 함수를 duration_ms 열의 각 항목에 적용
df_IU_top_track['duration_ms'] = df_IU_top_track['duration_ms'].apply(convert_msec) 

# duration_ms 열 이름을 duration로 변경
df_IU_top_track.rename(columns={'duration_ms':'duration'}, inplace=True)
df_IU_top_track.head()


# In[ ]:


df_IU_top_track.columns = ["아티스트", "곡 제목", "곡의 길이", "곡 ID", "인기도"] # 열 제목을 변경
df_IU_top_track.head()


# [8장: 384페이지]

# In[ ]:


import pandas as pd

def get_artist_top_track(artist_id, country_code):
    # 인기곡 정보 JSON 객체 받기
    artist_top_tracks_data = get_spotify_artist_top_tracks(artist_id, country_code)
    # 인기곡 정보 JSON 데이터에서 곡 정보 객체 리스트 추출
    top_tracks = artist_top_tracks_data['tracks']

    # 리스트를 DataFrame 데이터로 변환
    df_artist_top_track = pd.DataFrame(top_tracks)
    # DataFrame 데이터에서 열 선택
    df_artist_top_track2 = df_artist_top_track[['artists','name', 'duration_ms', 'id', 'popularity']]
    
    df_artist_top_track3 = df_artist_top_track2.copy() # DataFrame 데이터 복사
    # get_artists() 함수를 artists 열의 각 항목에 적용
    df_artist_top_track3['artists'] = df_artist_top_track3['artists'].apply(get_artists)

    df_artist_top_track4 = df_artist_top_track3.copy() # DataFrame 데이터 복사
    # convert_msec() 함수를 duration_ms 열의 각 항목에 적용
    df_artist_top_track4['duration_ms'] = df_artist_top_track4['duration_ms'].apply(convert_msec)
    
    # duration_ms 열 이름을 duration로 변경
    df_artist_top_track4.rename(columns={'duration_ms':'duration'}, inplace=True)

    # 열 제목을 변경
    df_artist_top_track4.columns = ["아티스트", "곡 제목", "곡의 길이", "곡 ID", "인기도"]
    
    return df_artist_top_track4


# [8장: 385페이지]

# In[ ]:


artist_id = "3Nrfpe0tUJi4K4DXYWgMUX" # 방탄소년단(BTS)의 아티스트 ID  
country_code = "US" # 미국의 국가 코드

df_BTS_top_track = get_artist_top_track(artist_id, country_code)
df_BTS_top_track.head()


# #### 아티스트의 앨범 정보 가져오기

# [8장: 387페이지]

# In[ ]:


def get_spotify_artist_albums_tracks(artist_id, include_groups=None):

    url = "https://api.spotify.com/v1/artists/{id}/albums".format(id=artist_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)

    parameters = {"include_groups": include_groups}
    headers = {"Authorization": "Bearer " + ACCESS_TOKEN}
      
    if(include_groups==None): # 앨범 타입을 지정하지 않을 경우 params 인수 없이 호출
        r = requests.get(url, headers=headers)
    else:                     # 앨범 타입을 지정할 경우 params 인수 호출
        r = requests.get(url, params=parameters, headers=headers)

    return r.json()


# [8장: 388페이지]

# In[ ]:


import pandas as pd

artist_id = "3HqSLMAZ3g3d5poNaI7GOU" # 아이유의 아티스트 ID

# album, single, appears_on, compilation
include_groups = "album,single"

artist_albums_data = get_spotify_artist_albums_tracks(artist_id, include_groups)
# artist_albums_data = get_sptoify_artist_albums_tracks(artist_id)
artist_albums = artist_albums_data['items']

albums_info = []
for album in artist_albums:
    albums_name_release_date = {"name":album['name'],
                                "album_type":album['album_type'],
                                "release_date":album['release_date'],
                                "album_id":album['id'],}
    albums_info.append(albums_name_release_date)

df_albums = pd.DataFrame(albums_info)
df_albums[0:10]


# [8장: 389페이지]

# In[ ]:


df_albums[df_albums['album_type']=='album']


# In[ ]:


import pandas as pd

def get_artist_albums(artist_id, include_groups=None):
    
    artist_albums_data = get_spotify_artist_albums_tracks(artist_id, include_groups)
    artist_albums = artist_albums_data['items']

    albums_info = []
    for album in artist_albums:
        albums_name_release_date = {"name":album['name'],
                                    "album_type":album['album_type'],
                                    "release_date":album['release_date'],
                                    "album_id":album['id'],}
        albums_info.append(albums_name_release_date)

    df_albums = pd.DataFrame(albums_info)
    return df_albums


# [8장: 390페이지]

# In[ ]:


artist_id = "6OwKE9Ez6ALxpTaKcT5ayv" # 악동뮤지션(악뮤)의 아티스트 ID

df_AKMU_albums = get_artist_albums(artist_id)
df_AKMU_albums.head()


# ### 8.4.3 트랙 API로 곡 관련 정보 가져오기

# #### 트랙(곡) 정보 가져오기

# [8장: 393페이지]

# In[ ]:


import requests

def get_spotify_track_info(track_id):
    url = "https://api.spotify.com/v1/tracks/{id}".format(id=track_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)

    headers = {"Authorization": "Bearer " + ACCESS_TOKEN} # 헤더 생성
    r = requests.get(url, headers=headers) # GET 방법으로 요청해 응답받음

    return r.json()


# In[ ]:


track_id = "2bgTY4UwhfBYhGT4HUYStN" # 트랙 ID(방탄소년단 Butter)
track_data = get_spotify_track_info(track_id)

print("[트랙(곡) 정보]")
print("- 아티스트:", get_artists(track_data['artists'])) # get_artists() 함수 이용
print("- 트랙(곡) 제목:", track_data['name'])
print("- 발표일:", track_data['album']['release_date'])
print("- 트랙(곡) 길이:", convert_msec(track_data['duration_ms'])) # convert_msec() 함수 이용
print("- 트랙 ID:", track_data['id'])
print("- 인기도:", track_data['popularity'])


# #### 트랙(곡)의 오디오 특징 정보 가져오기

# [8장: 396페이지]

# In[ ]:


import requests

def get_spotify_audio_features(track_id):
    url = "https://api.spotify.com/v1/audio-features/{id}".format(id=track_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)

    headers = {"Authorization": "Bearer " + ACCESS_TOKEN} # 헤더 생성
    r = requests.get(url, headers=headers) # GET 방법으로 요청해 응답받음

    return r.json()


# In[ ]:


track_id = "2bgTY4UwhfBYhGT4HUYStN" # 트랙 ID(방탄소년단 Butter)
audio_features_data = get_spotify_audio_features(track_id)
audio_features_data


# [8장: 397페이지]

# In[ ]:


import pandas as pd 

track_IDs = ["2bgTY4UwhfBYhGT4HUYStN", # 방탄소년단 Butter
             "3P3UA61WRQqwCXaoFOTENd", # 아이유 밤편지
             "5FKdWT5A7vDTEnPiHrruFY", # 김동률 출발
             "4ribiWWnI451QMRdOgByIP", # 이무진 비와 당신
             "1s6GWG2BrEWLE8sbd1lXME", # 악뮤 오랜 날 오랜 밤
             "4t2FIqZJORKZGSKg30SShr", # 악뮤(with IU) 낙하
             "1iIhGHzzrzqQfuNkFI2qAn", # 지코 아무 노래
             "4XaG9IpCXklOcuau1sIrUX", # 퀸(Queen) We Are The Champions
             "7vd1j4IDTU0koES9M8dvBQ", # 이루마 Kiss The Rain
             "3L1Ssz5HaOV3ZG9eJnV8UY"] # 피아노 캐논 변주곡
 
tracks_audio_features = [] # 여러 곡의 오디오 특징 리스트

for track_ID in track_IDs:
    # 아티스트와 트랙 이름 가져오기
    track_info = get_spotify_track_info(track_ID)
    
    # 트랙의 오디오 특징을 가져오기
    audio_features = get_spotify_audio_features(track_ID)
    
    # 아티스트와 트랙 정보와 오디오 특징 통합
    track_audio_features = {"artists":get_artists(track_info['artists']), 
                            "title":track_info['name'], 
                            "danceability":audio_features['danceability'],
                            "energy":audio_features['energy'],
                            "valence":audio_features['valence'],
                            "acousticness":audio_features['acousticness'],
                            "speechiness":audio_features['speechiness'],
                            "instrumentalness":audio_features['instrumentalness'],
                            "liveness":audio_features['liveness']}
    
    # 트랙의 오디오 특징 정보를 리스트에 담기
    tracks_audio_features.append(track_audio_features)
    
# DataFrame 데이터로 변환
df_tracks_audio_features = pd.DataFrame(tracks_audio_features)
df_tracks_audio_features


# [8장: 399페이지]

# In[ ]:


import matplotlib as mpl

mpl.rcParams['font.family'] = 'Malgun Gothic' # '맑은 고딕'으로 폰트 설정 
mpl.rcParams['axes.unicode_minus'] = False   # 마이너스(-) 폰트 깨짐 방지


# [8장: 400페이지]

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# 이제 오디오 특징 중 몇 가지를 선택해 막대 그래프로 비교해 보겠습니다.

# In[ ]:


import matplotlib.pyplot as plt

selected_columns = ["danceability", "energy", "valence", "acousticness",
                    "speechiness", "instrumentalness", "liveness"]
df_tracks_audio_features2 = df_tracks_audio_features[selected_columns]

ax = df_tracks_audio_features2.T.plot.bar(figsize=(15,4))
ax.legend(df_tracks_audio_features["title"],  bbox_to_anchor=(0.55, 0.2))

# x축 라벨, y축 라벨, title 지정 
ax.set_xlabel('오디오 특징', fontsize = 15)
ax.set_ylabel('값', fontsize = 15)
ax.set_title('트랙별 오디오 특징 비교', fontsize = 18)

plt.show()

# ### 8.4.4  앨범 API로 앨범 관련 정보 가져오기

# #### 앨범 정보 가져오기 

# [8장: 404페이지]

# In[ ]:


def get_spotify_album_info(album_id):
    url = "https://api.spotify.com/v1/albums/{id}".format(id=album_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)

    headers = {"Authorization": "Bearer " + ACCESS_TOKEN} # 헤더 생성

    r = requests.get(url, headers=headers) # GET 방법으로 응답을 요청

    return r.json()


# In[ ]:


album_id = "01dPJcwyht77brL4JQiR8R" # 앨범 ID(아이유 IU 5th Album 'LILAC' 앨범)

album_data = get_spotify_album_info(album_id)
album_data.keys()


# [8장: 405페이지]

# In[ ]:


print("[앨범 정보]")
print("- 아티스트:", get_artists(album_data['artists'])) # get_artists() 함수 이용
print("- 앨범 제목:", album_data['name'])
print("- 앨범 발표일:", album_data['release_date'])
print("- 앨범의 곡 개수:", album_data['total_tracks']) 
print("- 앨범 ID:", album_data['id'])
print("- 앨범 인기도:", album_data['popularity'])
print("- 앨범 Label:", album_data['label'])


# #### 앨범의 트랙(곡) 정보 가져오기 

# [8장: 407페이지]

# In[ ]:


def get_spotify_album_tracks(album_id):
    url = "https://api.spotify.com/v1/albums/{id}/tracks".format(id=album_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)

    headers = {"Authorization": "Bearer " + ACCESS_TOKEN} # 헤더 생성

    r = requests.get(url, headers=headers) # GET 방법으로 요청해 응답받음

    return r.json()


# In[ ]:


album_id = "01dPJcwyht77brL4JQiR8R" # 앨범 ID(아이유 IU 5th Album 'LILAC' 앨범)

album_tracks_data = get_spotify_album_tracks(album_id)

print("[앨범 트랙 정보]")
print("- 앨범 트랙 API URL:", album_tracks_data['href'])
print("- 설정한 트랙 수 :", album_tracks_data['limit']) 
print("- 설정한 트랙 오프셋:", album_tracks_data['offset']) 
print("- 앨범의 곡 개수:", album_tracks_data['total']) 
print("- 다음 트랙 API URL:", album_tracks_data['next']) 


# [8장: 408페이지]

# In[ ]:


import pandas as pd

def get_album_track(album_id):    
    album_tracks_data = get_spotify_album_tracks(album_id)
    album_tracks = album_tracks_data['items']

    df_album_tracks = pd.DataFrame(album_tracks) # DataFrame 데이터로 변환
    
    df_album_tracks2 = df_album_tracks[['artists', 'name', 'duration_ms', 'id']] # DataFrame 데이터에서 열 선택
    
    df_album_tracks3 = df_album_tracks2.copy() # DataFrame 데이터 복사
    df_album_tracks3['artists'] = df_album_tracks3['artists'].apply(get_artists) # 함수를 artists 열의 각 항목에 적용

    df_album_tracks4 = df_album_tracks3.copy() # DataFrame 데이터 복사
    df_album_tracks4['duration_ms'] = df_album_tracks4['duration_ms'].apply(convert_msec) # 함수를 artists 열의 각 항목에 적용
    df_album_tracks4.rename(columns = {'duration_ms' : 'duration'}, inplace = True) # duration_ms 열 이름을 duration로 변경

    df_album_tracks4.columns = ["아티스트", "곡 제목", "곡의 길이", "곡 ID"] # 열 제목을 변경
    
    return df_album_tracks4


# In[ ]:


album_id = "01dPJcwyht77brL4JQiR8R" # 앨범 ID(아이유 IU 5th Album 'LILAC' 앨범)

df_IU_album_tracks = get_album_track(album_id)
df_IU_album_tracks.head()

