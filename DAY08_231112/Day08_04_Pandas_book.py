# p.149 (2) 시리즈와 데이터프레임 이해하기
#222-01 판다스 임포트
import pandas as pd

#222-02 시리즈
s = pd.Series([1, 3, 5, 6, 8])
print(s)
print(s.index)
print(s.values)

#222-03 데이터프레임
v = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i = ['첫째행', '둘째행', '셋째행']
c = ['칼럼1', '칼럼2', '칼럼3']

df = pd.DataFrame(v, index=i, columns=c)
print(df)

# (3) 데이터프레임 생성하기
#223-01 리스트로 생성하기
d = [
    ['100', '강백호', 9.7],
    ['101', '송태섭', 8.9],
    ['102', '서태웅', 9.3],
    ['103', '채치수', 6.1]
]
df = pd.DataFrame(d, columns= ['번호', '이름', '점수'])
print(df)

#223-02 딕셔너리로 생성하기
d = {
    '번호' : ['100', '101', '102', '103'],
    '이름' : ['강백호', '송태섭', '서태웅', '채치수'],
    '점수' : [9.7, 8.9, 9.3, 6.1]
}
df = pd.DataFrame(d)
print(df)

#223-03 csv 파일로 생성하기
housing_df = pd.read_csv('data/california_housing_train.csv')
print('housing 변수 type : ', type(housing_df))
print(housing_df)

# (4) 데이터프레임 훑어보기
#224-01 데이터프레임 head 함수
print('DataFrame 크기 : ', housing_df.shape)
print(housing_df.head())

#224-02 데이터프레임 info 함수
print(housing_df.info())

#224-03 데이터프레임 describe 함수
print(housing_df.describe())

#224-04 시리즈 head 함수
housing_median_age = housing_df['housing_median_age']
print(housing_median_age.head())

#224-05 시리즈 value_counts 함수
value_counts = housing_median_age.value_counts()
print(value_counts)

# (5) 데이터프레임 칼럼 생성과 수정
#225-01 신규 칼럼 생성하기 기본
housing_df['Age_0'] = 0
print(housing_df.head())

#225-02 신규 칼럼 생성하기 응용
housing_df['Age_by_10'] = housing_df['housing_median_age'] // 10
print(housing_df.head())

#225-03 칼럼 데이터 수정하기
housing_df['Age_by_10'] = housing_df['Age_by_10'] * 10
print(housing_df.head())

#225-04 신규 칼럼 value_counts 함수
value_counts = housing_df['Age_by_10'].value_counts()
print(value_counts)

# (6) 데이터프레임 데이터 삭제
#226-01 칼럼 데이터 삭제하기
housing_drop_df = housing_df.drop('Age_0', axis=1)
housing_drop_df.head()

#226-02 복수 칼럼 데이터 삭제하기
drop_result = housing_df.drop(['Age_0', 'Age_by_10'], axis=1, inplace = True)
print('drop_result 반환값 : ', drop_result)
print(housing_df.head(3))

#226-03 행 데이터 삭제하기
housing_drop_df = housing_df.drop([0, 1, 2], axis =0)
print(housing_drop_df.head())

# (7) 데이터프레임 데이터 조회
#227-01 칼럼명으로 데이터 조회
print('단일 컬럼 데이터 조회 : \n', housing_df['housing_median_age'].head())
print('복수 칼럼 데이터 조회 : \n', housing_df[['housing_median_age', 'total_rooms']].head())

#227-02 인덱스 슬라이싱으로 데이터 조회
print(housing_df[0:3])

#227-03 논리형 인덱싱으로 데이터 조회
cond = housing_df['housing_median_age'] == 30
housing_df[cond].head()

#227-04 복수 논리형 인덱싱으로 데이터 조회
cond1 = housing_df['housing_median_age'] > 30
cond2 = housing_df['total_rooms'] < 100
cond3 = housing_df['median_income'] > 10
housing_df[(cond1 & cond2 & cond3)].head()

#227-06 iloc 함수로 데이터 조회
housing_df.iloc[0, 2]

#227-07 loc 함수로 데이터 조회
housing_df.loc[0, 'housing_median_age']

#227-08 loc 함수로 복수 데이터 조회
housing_df.loc[0 : 4, 'housing_median_age']

#227-09 loc 함수로 조건부 데이터 조회
cond = housing_df['housing_median_age'] == 30
housing_df.loc[cond, ['housing_median_age', 'total_bedrooms']].head()

# (8) 데이터프렝미 데이터 정렬과 집계
#228-01 오름차순 정렬
housing_sorted = housing_df.sort_values(by = ['housing_median_age'])
housing_sorted.head()

#228-02 복수 칼럼 내림차순 정렬
housing_df.sort_values(by = ['housing_median_age', 'total_rooms'], ascending = False)

#228-03 집계 함수 적용
housing_df.sum() / housing_df.count()

#228-04 특정 칼럼 집계 함수 적용
housing_df[['housing_median_age', 'total_rooms']].mean()

#228-05 groupby 함수 적용
housing_df.groupby('housing_median_age').mean().head()

#228-06 특정 칼럼 groupby 함수 적용
housing_df.groupby('housing_median_age')[['total_rooms', 'total_bedrooms']].mean().head()

#228-07 특정 칼럼 groupby, agg 함수 적용
housing_df.groupby('housing_median_age')['total_rooms'].agg([min, max, sum]).head()

# (9) 데이터프레임 결측치 처리하기
#229-01 결측치 여부 확인
import numpy as np
housing_df['Age_na'] = np.nan
housing_df.isna().head()

#229-02 결측치 개수 확인
housing_df.isna().sum()

#229-03 결측치 데이터 대체하기
housing_df['Age_na'] = housing_df['Age_na'].fillna(housing_df['housing_median_age'].mean())
housing_df.head()