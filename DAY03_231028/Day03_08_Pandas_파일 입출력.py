# 파일 입출력
import pandas as pd

from opendata import dataset
dataset.download('서울시주민등록인구')

#CSV - 불러오기
df = pd.read_csv('data/서울시주민등록인구/seoul_population.csv')
df

#CSV - 저장하기
df.to_csv('sample.csv', index=False)


# 조회, 정렬, 조건필터(with타이타닉호 데이터)
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
df.head()
df.tail()

df.head(3)
df.tail(7)

df.info()

df['who'].value_counts()

df.ndim

df.shape

df.index

df.columns

df.values

df.T

df['pclass'].astype('int32').head()

df['pclass'].astype('float32').head()

df['pclass'].astype('str').head()

df['pclass'].astype('category').head()

df.sort_index().head()

df.sort_index(ascending=False).head()

df.sort_values(by='age').head()

df.sort_values(by='age', ascending=False).head()

df.sort_values(by='class', ascending=False).head()

df.sort_values(by=['fare', 'age']).head()

df.sort_values(by=['fare', 'age'], ascending=[False, True]).head()


