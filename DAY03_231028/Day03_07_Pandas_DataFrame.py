# 데이터프레임
"""
1) 2차원 데이터 구조
2) 행(row), 열(column)으로 구성되어 있음
3) 각 열은 각각의 데이터 타입(dtype)을 가짐.
"""

# 생성
import pandas as pd

pd.DataFrame([[1,2,3],
                       [4,5,6],
                       [7,8,9]])

pd.DataFrame([[1,2,3],
                       [4,5,6],
                       [7,8,9]], columns=['가', '나', '다'])

data = {
    'name' : ['Kim', 'Lee', 'Park'],
    'age' : [24, 27, 34],
    'children' : [2, 1, 3]
}

pd.DataFrame(data)


#속성
"""
 index : index (기본 값으로 RangeIndex)
 columns : column 명
 values : numpy array형식의 데이터 값
 dtypes : column 별 데이터 타입
 T : DataFrame을 전치(Transpose)
 """
df = pd.DataFrame(data)
df.index
df.columns
df.values
df.dtypes
df.T

# index 지정
df.index = list('abd')
df

#column 다루기
df['name']
type(df['name'])
df[['name', 'children']]

df.rename(columns={'name': '이름'})   # 기존 df는 변경되지 않음
df.rename(columns={'name': '이름'}, inplace=True)  # 변경사항을 바로 적용


# 연습문제
#1번
import pandas as pd
df = pd.DataFrame([["KFC", 1000, 4.5],
                  ["McDonald", 2000, 3.9],
                  ["SchoolFood", 2500, 4.2]], columns=["food","price","rating"])
df

#2번
df[["food","rating"]]

#3번
df.rename(columns={"food" : "place"}, inplace=True)
df
