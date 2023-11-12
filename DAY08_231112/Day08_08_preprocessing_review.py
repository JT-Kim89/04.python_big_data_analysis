"""
https://www.datamanim.com/dataset/03_dataq/index_big_python.html
1. 빅데이터 분석기사 실기(Python)
1.2 데이터 전처리 100 문제
01 Getting & Knowing Data
"""
import pandas as pd

#Q1 데이터를 로드하라. 데이터는 \t을 기준으로 구분되어있다. - O
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(DataUrl, sep='\t')
df

#Q3 데이터의 행과 열의 갯수를 파악하라 - O
df.shape
print('행: ', df.shape[0])
print('열: ', df.shape[1])

#Q6 6번째 컬럼의 데이터 타입을 확인하라 - X
# 나 : df.columns[5].dtype
df.iloc[:,5].dtype #정답

#Q8 6번째 컬럼의 3번째 값은 무엇인가? - O
df.iloc[2,5]

# 제주 날씨,인구에 따른 교통량데이터 : 출처 제주 데이터 허브 DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv’
#Q9 데이터를 로드하라. 컬럼이 한글이기에 적절한 처리해줘야함 - X
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv'
df = pd.read_csv(DataUrl, encoding='euc-kr')

#Q11 수치형 변수를 가진 컬럼을 출력하라 - X (기억 안남)
df.select_dtypes(exclude=object).columns

#Q12 범주형 변수를 가진 컬럼을 출력하라 - X (기억 안남)
df.select_dtypes(include=object).columns

#Q13 각 컬럼의 결측치 숫자를 파악하라 - O
df.isnull().sum()

#Q14 각 컬럼의 데이터수, 데이터타입을 한번에 확인하라 - O
df.info()

#Q18 읍면동명 컬럼의 유일값 갯수를 출력하라 - O
df['읍면동명'].nunique()

#02 Filtering & Sorting
#Q20 데이터를 로드하라. - O
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
df = pd.read_csv(DataUrl)

#Q21 quantity컬럼 값이 3인 데이터를 추출하여 첫 5행을 출력하라 - O
cond = df['quantity'] == 3
df.loc[cond].head()

#Q22 quantity컬럼 값이 3인 데이터를 추출하여 index를 0부터 정렬하고 첫 5행을 출력하라 - O
df.loc[cond].reset_index(drop=True).head()

#Q23 quantity, item_price 두개의 컬럼으로 구성된 새로운 데이터 프레임을 정의하라 - O
df[['quantity', 'item_price']]

#Q24 item_price 컬럼의 달러표시 문자를 제거하고 float 타입으로 저장하여 new_price 컬럼에 저장하라 - O
df['new_price'] = df['item_price'].str[1:].astype(float)
df['new_price']

#Q26 item_name명이 Chicken Salad Bowl 인 데이터 프레임을 추출하라고 index 값을 초기화 하여라 - O
cond = df['item_name'] == 'Chicken Salad Bowl'
df.loc[cond].reset_index(drop=True)

#Q27 new_price값이 9 이하이고 item_name 값이 Chicken Salad Bowl 인 데이터 프레임을 추출하라 - O
cond1 = df['new_price'] <= 9
cond2 = df['item_name'] == 'Chicken Salad Bowl'
df.loc[(cond1 & cond2)]

#Q29 df의 item_name 컬럼 값 중 Chips 포함하는 경우의 데이터를 출력하라 - O
cond = df['item_name'].str.contains('Chips')
df.loc[cond]

#Q30 df의 짝수번째 컬럼만을 포함하는 데이터프레임을 출력하라 - O
df.iloc[:,::2]

#Q31 df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index를 초기화 하여라 - O
df.sort_values(by='new_price', ascending=False).reset_index(drop=True)

#Q33 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후,
# item_name를 기준으로 중복행이 있으면 제거하되 첫번째 케이스만 남겨라 - X
cond1 = df['item_name'] == 'Steak Salad'
cond2 = df['item_name'] == 'Bowl'
df2 = df.loc[(cond1 | cond2)]
df2['item_name'].drop_duplicates()  # 오답

df2.drop_duplicates('item_name')    # 정답

#Q34 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후,
# item_name를 기준으로 중복행이 있으면 제거하되 마지막 케이스만 남겨라 - X
df2 = df.loc[(cond1 | cond2)]
df2.drop_duplicates('item_name', keep='last') # keep='last' 기억 안남..

#Q36 df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy Lizzy로 수정하라 - X
cond = df['item_name'] == 'Izze'
df.loc[cond, 'item_name'] = 'Fizzy Lizzy'  # cond 다음 'item_name' 누락
df['item_name']

#Q38 df의 데이터 중 choice_description 값이 NaN 인 데이터를 NoData 값으로 대체하라(loc 이용) - O
cond = df['choice_description'].isnull()
df.loc[cond, 'choice_description'] = 'NoData'
df['choice_description']

#Q39 df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 인덱싱하라 - O
cond = df['choice_description'].str.contains('Black')
df.loc[cond]

#Q40 df의 데이터 중 choice_description 값에 Vegetables 들어가지 않는 경우의 갯수를 출력하라 - O
cond = ~df['choice_description'].str.contains('Vegetables')
len(df.loc[cond])

#Q41 df의 데이터 중 item_name 값이 N으로 시작하는 데이터를 모두 추출하라 - O
cond = df['item_name'].str.startswith('N')
df.loc[cond]

#Q43 df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라 - X
lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
cond = df['new_price'].isin(lst)        # isin() .. 기억안남
len(df.loc[cond])