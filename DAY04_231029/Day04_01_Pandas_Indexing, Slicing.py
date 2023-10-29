# indexing, Slicing
import numpy as np
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
"""
- indexing과 slicing을 할 수 있습니다.
- slicing은 [시작(포함):끝(포함)] 규칙에 유의합니다. 둘 다 포함 합니다.
"""

# Indexing, Slicing, 조건 필터링
df.loc[5, 'class']                          # indexing 예시
df.loc[2:5, ['age', 'fare', 'who']]     # fancy indexing 예시

df.loc[2:5, 'class':'deck'].head()      # slicing 예시

df.loc[:6, 'class':'deck']

# loc - 조건 필터
cond = (df['age'] >= 70)        # boolean index를 만들어 조건에 맞는 데이터만 추출할 수 있음
cond

df.loc[cond]
df.loc[cond, 'age']     # 나이 칼럼만 가져옴
df.loc[cond, 'age'] = -1  # 조건 필터 후 데이터 변경
df.loc[cond, 'age']     # 나이 칼럼만 가져옴


# loc - 다중 조건
cond1 = (df['fare'] > 30) # 조건1 정의
cond2 = (df['who'] == 'woman') # 조건2 정의

df.loc[cond1 & cond2]  # and
df.loc[cond1 | cond2]  # or


# iloc
df.iloc[1,3]        # indexing
df.iloc[[0,3,4],[0,1,5,6]]      # Fancy Indexing

# Slicing
df.iloc[:3, :5]



# isin : 특정 값의 포함 여부
sample = pd.DataFrame({'name': ['kim', 'lee', 'park', 'choi'],
                                     'age' : [24, 27, 34, 19]})

sample

sample['name'].isin(['kim', 'lee'])
sample.isin(['kim', 'lee'])

condition = sample['name'].isin(['kim', 'lee'])
sample.loc[condition]



