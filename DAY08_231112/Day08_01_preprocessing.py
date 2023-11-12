"""
https://www.datamanim.com/dataset/03_dataq/index_big_python.html
1. 빅데이터 분석기사 실기(Python)
1.2 데이터 전처리 100 문제
01 Getting & Knowing Data
"""
import pandas as pd

#Q1 데이터를 로드하라. 데이터는 \t을 기준으로 구분되어있다. - X
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(DataUrl, sep='\t')
type(df)

#Q2 데이터의 상위 5개 행을 출력하라 - O
df.head(5)

#Q3 데이터의 행과 열의 갯수를 파악하라 - X
print(df.shape)
print('행:', df.shape[0])
print('열:', df.shape[1])

#Q4 전체 컬럼을 출력하라 - O
print(df.columns)

#Q5 6번째 컬럼명을 출력하라 - O
print(df.columns[5])

#Q6 6번째 컬럼의 데이터 타입을 확인하라 - X
df.iloc[:,5].dtype

#Q7 데이터셋의 인덱스 구성은 어떤가 - O
df.index

#Q8 6번째 컬럼의 3번째 값은 무엇인가? - X
df.iloc[2,5]

# 제주 날씨,인구에 따른 교통량데이터 : 출처 제주 데이터 허브 DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv’
#Q9 데이터를 로드하라. 컬럼이 한글이기에 적절한 처리해줘야함 - ?X
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv'
df = pd.read_csv(DataUrl, encoding='euc-kr')

#Q10 데이터 마지막 3개행을 출력하라 - O
df.tail(3)

#Q11 수치형 변수를 가진 컬럼을 출력하라 - ???
df.select_dtypes(exclude=object).columns

#Q12 범주형 변수를 가진 컬럼을 출력하라 - ???
df.select_dtypes(include=object).columns

#Q13 각 컬럼의 결측치 숫자를 파악하라 - X
df.isnull().sum()

#Q14 각 컬럼의 데이터수, 데이터타입을 한번에 확인하라 - X
df.info()

#Q15 각 수치형 변수의 분포(사분위, 평균, 표준편차, 최대 , 최소)를 확인하라 - O
df.describe()

#Q16 거주인구 컬럼의 값들을 출력하라 - O
df['거주인구']

#Q17 평균 속도 컬럼의 4분위 범위(IQR) 값을 구하여라 - O
df
df['평균 속도'].quantile(0.75) - df['평균 속도'].quantile(0.25)

#Q18 읍면동명 컬럼의 유일값 갯수를 출력하라 - X
df['읍면동명'].nunique()
# -> 유일값 개수 : ~~~.nunique()


#Q19 읍면동명 컬럼의 유일값을 모두 출력하라 - O
df['읍면동명'].unique()

#02 Filtering & Sorting
#Q20 데이터를 로드하라. - O
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
df = pd.read_csv(DataUrl)

#Q21 quantity컬럼 값이 3인 데이터를 추출하여 첫 5행을 출력하라 - X
df.loc[df['quantity']==3].head()

#Q22 quantity컬럼 값이 3인 데이터를 추출하여 index를 0부터 정렬하고 첫 5행을 출력하라 - X
df.loc[df['quantity']==3].head().reset_index(drop=True)

#Q23 quantity , item_price 두개의 컬럼으로 구성된 새로운 데이터 프레임을 정의하라 - X
df2 = df[['quantity', 'item_price']]
df2
# -> df[ ['칼럼1', '칼럼2'] ]

#Q24 item_price 컬럼의 달러표시 문자를 제거하고 float 타입으로 저장하여 new_price 컬럼에 저장하라 - O
df['new_price'] = df['item_price'].str[1:].astype(float)
df['new_price'].head()

#Q25 new_price 컬럼이 5이하의 값을 가지는 데이터프레임을 추출하고, 전체 갯수를 구하여라 - O
df['new_price'].loc[df['new_price'] <= 5].count()
# 답지 : len(df.loc[df.new_price <= 5])

#Q26 item_name명이 Chicken Salad Bowl 인 데이터 프레임을 추출하라고 index 값을 초기화 하여라 - X
df.loc[df['item_name'] == 'Chicken Salad Bowl'].reset_index(drop=True)
# -> reset_index(drop=True)

#Q27 new_price값이 9 이하이고 item_name 값이 Chicken Salad Bowl 인 데이터 프레임을 추출하라 - X
df.loc[(df['new_price'] <= 9) & (df['item_name'] == 'Chicken Salad Bowl')].head()
# -> (조건1) & (조건2)

#Q28 df의 new_price 컬럼 값에 따라 오름차순으로 정리하고 index를 초기화 하여라 - O
df.sort_values(by='new_price').reset_index(drop=True).head(4)

#Q29 df의 item_name 컬럼 값 중 Chips 포함하는 경우의 데이터를 출력하라 - ???
df.loc[df['item_name'].str.contains('Chips')].head()
# -> str.contains('포함할 문자')

#Q30 df의 짝수번째 컬럼만을 포함하는 데이터프레임을 출력하라 - X
df.iloc[:,::2].head()
# -> iloc[행, 열]

#Q31 df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index를 초기화 하여라 - X
df.sort_values(by='new_price', ascending=False).reset_index(drop='True')
# -> ascending=False

#Q32 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 인덱싱하라 - O
df.loc[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')]

#Q33 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후,
# item_name를 기준으로 중복행이 있으면 제거하되 첫번째 케이스만 남겨라 - ???
df2 = df.loc[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')]
df2.drop_duplicates('item_name')  # 외우기

#Q34 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후,
# item_name를 기준으로 중복행이 있으면 제거하되 마지막 케이스만 남겨라 -???
df2 = df.loc[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')]
df2.drop_duplicates('item_name', keep='last')

#Q35 df의 데이터 중 new_price값이 new_price값의 평균값 이상을 가지는 데이터들을 인덱싱하라 - O
cond = df['new_price'] >= df['new_price'].mean()
df.loc[cond].head()

#Q36 df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy Lizzy로 수정하라 - ???
cond = df['item_name'] == 'Izze'
df.loc[cond, 'item_name'] = 'Fizzy Lizzy'
df.item_name.head(3)

#Q37 df의 데이터 중 choice_description 값이 NaN 인 데이터의 갯수를 구하여라 - O
df['choice_description'].isnull().sum()

#Q38 df의 데이터 중 choice_description 값이 NaN 인 데이터를 NoData 값으로 대체하라(loc 이용) - X
cond = df['choice_description'].isnull()
df.loc[cond, 'choice_description'] = 'NoData'  # == 으로 작성하여 틀림
df.choice_description.head()

#Q39 df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 인덱싱하라 - X
df[df['choice_description'].str.contains('Black')].head()
#-> loc 사용하지 않음...

#Q40 df의 데이터 중 choice_description 값에 Vegetables 들어가지 않는 경우의 갯수를 출력하라 - ???
cond = ~df['choice_description'].str.contains('Vegetables')   # ~ : 여집합
len(df.loc[cond])

#Q41 df의 데이터 중 item_name 값이 N으로 시작하는 데이터를 모두 추출하라 - ???
cond = df['item_name'].str.startswith('N') # str.startswith('문자') : '문자'로 시작하는 문자열
df[cond].head(3)

#Q42 df의 데이터 중 item_name 값의 단어갯수가 15개 이상인 데이터를 인덱싱하라 - O
cond = df['item_name'].str.len() >= 15
df[cond].head(3)

#Q43 df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라 - ???
lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
cond = df['new_price'].isin(lst)  # isin() : 포함되었는지
df[cond].head(3)
len(df[cond])

#03 Grouping
#Q44 데이터를 로드하고 상위 5개 컬럼을 출력하라 - O
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv'
df = pd.read_csv(DataUrl)
df.head()

#Q45 데이터의 각 host_name의 빈도수를 구하고 host_name으로 정렬하여 상위 5개를 출력하라 - ???
df.groupby('host_name').size().head()                   # 정답1 groupby 사용
df['host_name'].value_counts().sort_index().head() # 정답2 기존 방법

#Q46 데이터의 각 host_name의 빈도수를 구하고 빈도수 기준 내림차순 정렬한 데이터 프레임을 만들어라. - ???
#빈도수 컬럼은 counts로 명명하라
df.groupby('host_name').size().\
    to_frame().rename(columns={0:'counts'}).\
    sort_values('counts', ascending=False).head()

#Q47 neighbourhood_group의 값에 따른 neighbourhood컬럼 값의 갯수를 구하여라 - ???
df.groupby(['neighbourhood_group', 'neighbourhood'], as_index=False).size()

#Q48 neighbourhood_group의 값에 따른 neighbourhood컬럼 값 중 neighbourhood_group그룹의 최댓값들을 출력하라


#Q49 neighbourhood_group 값에 따른 price값의 평균, 분산, 최대, 최소 값을 구하여라
df.groupby('neighbourhood_group')['price'].agg(['mean', 'var', 'max', 'min'])

Ans = df[['neighbourhood_group','price']].groupby('neighbourhood_group').agg(['mean','var','max','min'])
Ans

#Q50 neighbourhood_group 값에 따른 reviews_per_month 평균, 분산, 최대, 최소 값을 구하여라
df.groupby('neighbourhood_group')['reviews_per_month'].agg(['mean', 'var', 'max', 'min'])

#Q51

#Q52

#Q53

#Q54

#Q55


# 04_Apply, Map
#Q56 데이터를 로드하고 데이터 행과 열의 갯수를 출력하라 - O
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv'
df = pd.read_csv(DataUrl)
df.shape
print('행: ', df.shape[0], '열: ', df.shape[1])

#Q57
#Q58
#Q59

#Q60
#Q61
#Q62
#Q63


# 05_Time_Series
#Q64 데이터를 로드하고 각 열의 데이터 타입을 파악하라
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv'
df = pd.read_csv(DataUrl)
df.info()

#Q65 Yr_Mo_Dy을 판다스에서 인식할 수 있는 datetime64타입으로 변경하라
df.Yr_Mo_Dy = df['Yr_Mo_Dy'].astype('datetime64')
df.info()

# 답지
df.Yr_Mo_Dy = pd.to_datetime(df.Yr_Mo_Dy)

#Q66 Yr_Mo_Dy에 존재하는 년도의 유일값을 모두 출력하라
df['Yr_Mo_Dy'].dt.year.unique()  # dt.year : 연도 확인

#Q67Yr_Mo_Dy에 년도가 2061년 이상의 경우에는 모두 잘못된 데이터이다.
# 해당경우의 값은 100을 빼서 새롭게 날짜를 Yr_Mo_Dy 컬럼에 정의하라

help(pd.read_csv)


#Q68
#Q69

#Q70
#Q71
#Q72
#Q73
#Q74
#Q75
#Q76
#Q77
#Q78
#Q79

#Q80
#Q81
#Q82
#Q83
#Q84
#Q85
#Q86
#Q87
#Q88
#Q89

#Q90
#Q91
#Q92
#Q93
#Q94
#Q95
#Q96
#Q97
#Q98
#Q99
#Q100
