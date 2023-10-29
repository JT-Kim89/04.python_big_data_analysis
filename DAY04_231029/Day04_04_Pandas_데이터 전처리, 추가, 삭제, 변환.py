# 데이터 전처리, 추가, 삭제, 변환
import numpy as np

import seaborn as sns
df = sns.load_dataset('titanic')
df.head()

df1 = df.copy()
df1['VIP'] = True           # 새로운 칼럼 추가
df1.head()

df1.insert(5, 'RICH', df1['fare'] > 100)    # 중간에 칼럼을 추가하고 싶은 경우 insert() 활용
df1.head()

# 삭제
# 행삭제
df1.drop(1)     # index 지정
df1.drop(np.arange(10))         # 범위를 지정하여 삭제
df1.drop([1,3,5,7,9])               #  fancy indexing

# 열삭제 : 반드시 axis = 1 옵션을 지정해야 함
df1.drop('class', axis=1).head()
df1.drop('class', 1).head()         # axis= 를 생략할 수 있음.
df1.drop(['who', 'deck', 'alive'], axis=1)

df1.drop(['who', 'deck', 'alive'], axis=1, inplace=True)  # 변경된 내용은 바로 적용
df1.head()

# 칼럼간 연산
df1 = df.copy()
df1['family'] = 1 + df1['sibsp'] + df1['parch']
df1.head()

# 문자열의 합
df1['gender'] = df1['who'] + '-' + df1['sex']
df1.head()

# round(숫자, 소수 몇 째자리)
df1['round'] = round(df1['fare'] / df1['age'], 2)   # 계산 시 NaN값을 포함하고 있다면 결과는 NaN이 된다.
df1.head()

df1.loc[df1['age'].isnull(), 'age':].head()

# category 타입
df1 = df.copy()
df1.head(2)
df1.info()

df1['who'].astype('category').head()


