# 복사와 결측치
import numpy as np
import pandas as pd
import seaborn as sns

# 데이터셋 로드
df = sns.load_dataset('titanic')


# Copy (복사) : DataFrame을 복제함. 복제한 DataFrame을 수정해도 원본에는 영향을 미치지 않음.
df_copy = df.copy()
df_copy.head()

df_copy.loc[0, 'age'] = 99999
df_copy.head()  # 수정사항 반영된 것 확인
df.head()       # 원본 데이터는 변경되지 않고 그대로 남아 있음.

# 결측치
"""
결측치 : 비어있는 데이터
 1) 결측 데이터 확인
 2) 결측치가 아닌 데이터 확인
 3) 결측 데이터 채우기
 4) 결측 데이터 제거하기
"""

# 결측치 확인 - isnull(), isna()
df.isnull().sum()   # sum함수를 이용해 칼럼별 결측치 개수 확인
df.isna().sum()   # isnull()과 동일하므로 편한 것 사용

df.isnull().sum().sum()   # 전체 결측치 개수 확인


# 결측치가 아닌 데이터 확인 - notnull()
df.notnull().sum()

# 결측 데이터 필터링
df.loc[df['age'].isnull()]      # 결측 데이터만 분류

# 결측치 채우기 - fillna()
df_copy['age'].fillna(700).tail()       # 결측치를 700으로 채움

# 통계값으로 채우기
#1 평균으로 채우기
df1 = df.copy()
df1['age'].fillna(df1['age'].mean()).tail()

#2 중앙값으로 채우기
df1['age'].fillna(df1['age'].median()).tail()

#3 최빈값으로 채우기
df1['deck'].mode()
df1['deck'].mode()[0]       # 최빈값(mode)으로 채울 때에는 반드시 0번째 index를 지정하여 값 추출 후 사용
df1['deck'].fillna(df1['deck'].mode()[0]).tail()


# NaN 값이 있는 데이터 제거하기 (dropna)
df1 = df.copy()
df1.dropna()    # 1개라도 NaN 값이 있는 행은 제거함 (how = 'any')
df1.dropna(how='all')   # 모두 NaN값이면 drop


# 연습문제
#1번 문제
df1 = df.copy()
df1['age'].fillna(30)
df1.loc[df1['age'].isnull()]      # 결측 데이터만 분류

# 검증코드
# 본 Cell을 실행시 ERROR가 발생하지 않아야 함
df['age'].isnull().sum() == 0
df['age'].mean().round(4) == 29.7589





