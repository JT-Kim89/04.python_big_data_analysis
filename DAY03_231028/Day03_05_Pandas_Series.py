# 시리즈
import numpy as np
import pandas as pd
"""
Series는 1차원 배열로 아래의 특징을 가짐.
1) 데이터를 담는 차원 배열 구조를 가짐.
2) 인덱스(index)를 사용 가능
3) 데이터 타입(dtype)을 가짐
"""

# Series의 생성
arr = np.arange(100,105)    #numpy로 생성
arr

s = pd.Series(arr)
s

s = pd.Series(arr, dtype='int64')      # dtype을 지정하여 생성한 경우
s

#다양한 타입(type)의 데이터를 섞은 경우 -> object 타입으로 생성됨
s = pd.Series([91, 2.5, 'sport', 4, 5.16])
s

# list로 생성한 경우
s = pd.Series(['부장', '차장', '과장', '대리', '사원'])
s

# 인덱싱(indexing)
s.index
s[0]

# fancy indexing
s[[1, 3]]
s[np.arange(1,4,2)]

# boolean indexing : 조건식을 만들어서 특정 조건에 대하여 True에 해당하는 값만 필터링
np.random.seed(0)
s = pd.Series(np.random.randint(10000, 20000, size=(10,)))
s

s > 15000   # boolean series를 생성 후 index로 활용하여 필터링
s[s>15000] # 15000 이상인 데이터만 남김

s = pd.Series(['마케팅', '경영', '개발', '기획', '인사'], index=['a', 'b', 'c', 'd', 'e'])
s

s.index

s['c']

s[['a', 'd']]

s = pd.Series(['마케팅', '경영', '개발', '기획', '인사'])
s.index

s.index=list('abcde')
s


#속성 (attribute)
# values : Series 데이터 값(value)만 numpy array 형식으로 가져 옵니다.
s.values

#ndim - 차원
s.ndim

#shape : 데이터의 개수를 나타냄
s.shape

#NaN (Not a Number) : 결측치 데이터
s = pd.Series(['선화', '강호', np.nan, '소정', '우영'])
s

#결측치 값 처리
s.isnull()
s.isna()
s[s.isnull()]
s[s.isna()]

s.notnull()
s.notna()
s[s.notnull()]

#슬라이싱
s = pd.Series(np.arange(100, 150, 10))
s

s[1:3]

s.index = list('가나다라마')
s

s['나':'라']

