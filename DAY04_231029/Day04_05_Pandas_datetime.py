# datetime : 날짜, 시간 계산에 활용

import pandas as pd
from opendata import dataset
dataset.download('서울시자전거')

df2 = pd.read_csv('data/서울시자전거/seoul_bicycle.csv')
df2.head()

df2.info()  # 대여일자 칼럼을 object로 인식하고 있음
pd.to_datetime(df2['대여일자'])     # 대여일자를 datetime type으로 변경

df2['대여일자'] = pd.to_datetime(df2['대여일자']) # 원본 데이터에 반영

df2.info()

df2['대여일자'].dt.year      # '연'만 출력
df2['대여일자'].dt.month    # '월'만 출력
df2['대여일자'].dt.day       # '일'만 출력
df2['대여일자'].dt.dayofweek       # 요일


# pd.cut() - 구간 나누기(binning) : 연속된 수치(continuous values)를 구간으로 나누어 카테고리화 할 때 사용
bins = [0, 6000, 10000, df2['이동거리'].max()]
pd.cut(df2['이동거리'], bins, right=False)      # right=False로 지정 시 우측 범위를 포함하지 않음.
labels = ['적음', '보통', '많음']
pd.cut(df2['이동거리'], bins, labels=labels, right=False)

df2['이동거리_cut'] = pd.cut(df2['이동거리'], bins=3)
df2['이동거리_cut'].value_counts()

# pd.qcut() : 동일한 개수를 갖도록 구간 분할
df2['이동거리_cut'] = pd.qcut(df2['이동거리'], q=3)
df2['이동거리_cut'].value_counts()

qcut_bins = [0, 0.2, 0.8, 1]
pd.qcut(df2['이동거리'], qcut_bins)

qcut_labels = ['적음', '보통', '많음']
pd.qcut(df2['이동거리'], qcut_bins, labels=qcut_labels).value_counts()