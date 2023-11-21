#03 Grouping
"""
groupby() : 데이터를 특정 기준으로 그룹핑 할 때 활용
"""
import pandas as pd
import seaborn as sns
df = sns.load_dataset('titanic')
df.head()

# apply() - 함수 적용
df['who'].value_counts()

def transform_who(x):
    if x == 'man':
        return '남자'
    elif x == 'woman':
        return '여자'
    else :
        return '아이'

df['who'].apply(transform_who)
df['who'].apply(transform_who).value_counts()

def transform_who2(x):
    return x['fare'] / x['age']

df.apply(transform_who2, axis=1)

# apply() - lambda 함수
df['survived'].value_counts()  # 0: 사망, 1: 생존으로 변경
df['survived'].apply(lambda x: '생존' if x == 1 else '사망')
df['survived'].apply(lambda x: '생존' if x == 1 else '사망').value_counts()


# 1) Groupby() : aggregate 하는 통계함수와 같이 적용
df.groupby('sex').mean()  # 성별 평균

# 2개 이상의 칼럼으로 그룹
df.groupby(['sex', 'pclass']).mean() # 성별 분류 후 다시 탑승권 분류 평균

# 1개의 특정 칼럼에 대한 결과 도출
df.groupby(['sex', 'pclass'])['survived'].mean() # survived에 대한 결과만 확인

pd.DataFrame(df.groupby(['sex', 'pclass'])['survived'].mean()) # DataFrame으로 출력
df.groupby(['sex', 'pclass'])[['survived']].mean()

# reset_index() : 인덱스 초기화
df.groupby(['sex', 'pclass'])['survived'].mean().reset_index()

# 다중 칼럼에 대한 결과 도출
df.groupby(['sex', 'pclass'])[['survived', 'age']].mean() # survived, age의 평균값

# 다중 통계 함수 적용
df.groupby(['sex', 'pclass'])[['survived', 'age']].agg(['mean', 'sum']) # 2개 이상의 통계 분석 시 agg()로 묶어줌.


# 연습문제
sample = df.copy()
sample.head()
sample['class'].value_counts()

# apply()를 활용하여 class 칼럼의 값을 First : 일등석, Second : 이등석, Third 삼등석으로 변경
def class_kor(x):
    if x == "First":
        return "일등석"
    elif x == "Second":
        return "이등석"
    else:
        return "삼등석"

sample['class'].apply(class_kor).value_counts()

# groupby()를 활용하여 다음을 출력하세요.
# pclass 별 생존율
sample.groupby(['pclass']).survived.mean()

# embarked 별 생존율 통합 통계
sample.groupby(['embarked']).survived.agg(['mean', 'var'])

# who, pclass 별 생존율, 생존자수
sample.groupby(['who', 'pclass']).survived.agg(['mean', 'sum'])

# 남자의 나이는 남자 나이의 평균으로 채우고, 여자의 나이는 여자 나이의 평균으로 채움.
sample['age'].isnull().sum()
sample.groupby(['sex']).age.mean()
sample[['sex', 'age']].tail(15)

# 잘 모르겠음...
def mean_age(x):
    if x == 'male':
        return sample.groupby(['sex']).age.mean()[1]
    else:
        return sample.groupby(['sex']).age.mean()[0]

sample['age'].fillna(mean_age)

# 답안
sample['age'] = sample.groupby('sex')['age'].apply(lambda x: x.fillna(x.mean()))
sample['age'].isnull().sum()
sample['age'].mean()
sample[['sex', 'age']].tail(15)


#Q44 데이터를 로드하고 상위 5개 컬럼을 출력하라
pd.set_option('display.max_columns', None)
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv'
df = pd.read_csv(DataUrl)
df.head()

#Q45 데이터의 각 host_name의 빈도수를 구하고 host_name으로 정렬하여 상위 5개를 출력하라 - ???
df.groupby('host_name').size().head()
df["host_name"].value_counts().sort_index().head()

#Q46 데이터의 각 host_name의 빈도수를 구하고 빈도수 기준 내림차순 정렬한 데이터 프레임을 만들어라. - ???
#빈도수 컬럼은 counts로 명명하라
df.groupby('host_name').size() \
    .to_frame().rename(columns = {0: 'counts'}) \
    .sort_values('counts', ascending = False) \
    .head()

#Q47 neighbourhood_group의 값에 따른 neighbourhood컬럼 값의 갯수를 구하여라 - ???
df.groupby(['neighbourhood_group', 'neighbourhood'], as_index=False).size()


#Q48 neighbourhood_group의 값에 따른 neighbourhood컬럼 값 중 neighbourhood_group그룹의 최댓값들을 출력하라
df.groupby(['neighbourhood_group', 'neighbourhood'], as_index=False).size() \
    .groupby(['neighbourhood_group'], as_index=False).max()

#Q49 neighbourhood_group 값에 따른 price값의 평균, 분산, 최대, 최소 값을 구하여라
df.groupby('neighbourhood_group')[['price']].agg(['mean', 'var', 'max', 'min'])

#Q50 neighbourhood_group 값에 따른 reviews_per_month 평균, 분산, 최대, 최소 값을 구하여라
df.groupby('neighbourhood_group')[['reviews_per_month']].agg(['mean', 'var', 'max', 'min'])

#Q51 neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 구하라
df.groupby(['neighbourhood', 'neighbourhood_group'])['price'].mean()

#Q52 neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하라
df.groupby(['neighbourhood', 'neighbourhood_group'])['price'].mean().unstack()

#Q53 neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하고
# nan 값은 -999값으로 채워라
df.groupby(['neighbourhood', 'neighbourhood_group'])['price'].mean().unstack().isnull()
df.groupby(['neighbourhood', 'neighbourhood_group'])['price'].mean().unstack().fillna(-999)


#Q54 데이터중 neighbourhood_group 값이 Queens값을 가지는 데이터들 중
# neighbourhood 그룹별로 price값의 평균, 분산, 최대, 최소값을 구하라
df[df.neighbourhood_group=='Queens'] \
.groupby(['neighbourhood'])['price'].agg(['mean', 'var', 'max', 'min'])

#Q55 데이터중 neighbourhood_group 값에 따른 room_type 컬럼의 숫자를 구하고
# neighbourhood_group 값을 기준으로 각 값의 비율을 구하여라
Ans = df.groupby(['neighbourhood_group', 'room_type']).size().unstack()
Ans.loc[:,:] = (Ans.values / Ans.sum(axis=1).values.reshape(-1,1))
Ans

# 04_Apply, Map
#Q56 데이터를 로드하고 데이터 행과 열의 갯수를 출력하라 - O
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv'
df = pd.read_csv(DataUrl)
df.head()
df.shape

#Q57 Income_Category의 카테고리를 map 함수를 이용하여
# 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
"""
Unknown : N
Less than $40K : a
$40K - $60K : b
$60K - $80K : c
$80K - $120K : d
$120K +’ : e
"""
dic = {
    'Unknown'           : 'N',
    'Less than $40K' : 'a',
    '$40K - $60K'     : 'b',
    '$60K - $80K'     : 'c',
    '$80K - $120K'   : 'd',
    '$120K +'           : 'e'
}
df['newIncome'] = df.Income_Category.map(lambda x: dic[x])
df['newIncome']

#Q58 Income_Category의 카테고리를 apply 함수를 이용하여
# 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
def newIncome(x):
    if x == "Unknown":
        return "N"
    elif x == "Less than $40K":
        return 'a'
    elif x == '$40K - $60K':
        return 'b'
    elif x == '$60K - $80K':
        return 'c'
    elif x == '$80K - $120K':
        return 'd'
    else:
        return 'e'

df['newIncome'] = df.Income_Category.apply(newIncome)
df['newIncome']

#Q59 Customer_Age의 값을 이용하여 나이 구간을 AgeState 컬럼으로 정의하라.
# (0~9 : 0 , 10~19 :10 , 20~29 :20 … 각 구간의 빈도수를 출력하라
df['AgeState'] = df.Customer_Age.map(lambda x: x//10 * 10)
df['AgeState'].value_counts().sort_index()

#Q60 Education_Level의 값중 Graduate단어가 포함되는 값은 1 그렇지 않은 경우에는 0으로 변경하여
# newEduLevel 컬럼을 정의하고 빈도수를 출력하라
df['newEduLevel'] = df.Education_Level.map(lambda x: 1 if 'Graduate' in x else 0)
df['newEduLevel'].value_counts()

#Q61 Credit_Limit 컬럼값이 4500 이상인 경우 1 그외의 경우에는 모두 0으로 하는 newLimit 정의하라.
# newLimit 각 값들의 빈도수를 출력하라
df['newLimit'] = df.Credit_Limit.map(lambda x: 1 if x >= 4500 else 0)
df['newLimit'].value_counts()

#Q62 Marital_Status 컬럼값이 Married 이고 Card_Category 컬럼의 값이 Platinum인 경우 1
# 그외의 경우에는 모두 0으로 하는 newState컬럼을 정의하라.
# newState의 각 값들의 빈도수를 출력하라
def check(x):
    if x.Marital_Status == "Married" and x.Card_Category == 'Platinum':
        return 1
    else :
        return 0

df['newState'] = df.apply(check, axis=1)
df['newState'].value_counts()

#Q63 Gender 컬럼값 M인 경우 male F인 경우 female로 값을 변경하여
# Gender 컬럼에 새롭게 정의하라. 각 value의 빈도를 출력하라
def check(x):
    if x.Gender == "M":
        return "male"
    else :
        return "female"

df['Gender'] = df.apply(check, axis=1)
df['Gender'].value_counts()

# 05_Time_Series
#Q64 데이터를 로드하고 각 열의 데이터 타입을 파악하라
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv'
df = pd.read_csv(DataUrl)
df.info()

#Q65 Yr_Mo_Dy을 판다스에서 인식할 수 있는 datetime64타입으로 변경하라
df.Yr_Mo_Dy = pd.to_datetime(df.Yr_Mo_Dy)
df.info()

#Q66 Yr_Mo_Dy에 존재하는 년도의 유일값을 모두 출력하라
df.Yr_Mo_Dy.dt.year.unique()

#Q67 Yr_Mo_Dy에 년도가 2061년 이상의 경우에는 모두 잘못된 데이터이다.
# 해당경우의 값은 100을 빼서 새롭게 날짜를 Yr_Mo_Dy 컬럼에 정의하라
def fix_century(x):
    import datetime

    year = x.year - 100 if x.year >= 2061 else x.year
    return pd.to_datetime(datetime.date(year, x.month, x.day))

df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix_century)
df.head(4)

#Q68 년도별 각컬럼의 평균값을 구하여라
df.groupby(df.Yr_Mo_Dy.dt.year).mean()

#Q69 weekday컬럼을 만들고 요일별로 매핑하라 ( 월요일: 0 ~ 일요일 :6)
df['weekday'] = df.Yr_Mo_Dy.dt.weekday
df['weekday']

#Q70 weekday컬럼을 기준으로 주말이면 1 평일이면 0의 값을 가지는
# WeekCheck 컬럼을 만들어라
df['WeekCheck'] = df.weekday.map(lambda x : 1 if x in [5,6] else 0)
df['WeekCheck']

#Q71 년도, 일자 상관없이 모든 컬럼의 각 달의 평균을 구하여라
df.groupby(df.Yr_Mo_Dy.dt.month).mean()

#Q72 모든 결측치는 컬럼기준 직전의 값으로 대체하고
# 첫번째 행에 결측치가 있을경우 뒤에있는 값으로 대채하라
df = df.fillna(method='ffill').fillna(method='bfill')
df.isnull().sum()

#Q73 년도 - 월을 기준으로 모든 컬럼의 평균값을 구하여라
df.groupby(df.Yr_Mo_Dy.dt.to_period('M')).mean()

#Q74 RPT 컬럼의 값을 일자별 기준으로 1차차분하라
df['RPT'].diff()

#Q75 RPT와 VAL의 컬럼을 일주일 간격으로 각각 이동평균한값을 구하여라
df[['RPT', 'VAL']].rolling(7).mean()


# 서울시 미세먼지 데이터
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/seoul_pm.csv'
df = pd.read_csv(DataUrl)
df.info()

#Q76 년-월-일:시 컬럼을 pandas에서 인식할 수 있는 datetime 형태로 변경하라.
# 서울시의 제공데이터의 경우 0시가 24시로 표현된다
def change_date(x):
    import datetime
    hour = x.split(":")[1]
    date = x.split(":")[0]

    if hour == '24':
        hour = '00:00:00'

        FinalDate = pd.to_datetime(date + " "+hour) + datetime.timedelta(days=1)

    else:
        hour = hour +":00:00"
        FinalDate = pd.to_datetime(date + " "+hour)

    return FinalDate

df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change_date)
df

#Q77 일자별 영어요일 이름을 dayName 컬럼에 저장하라
df['dayName'] = df['(년-월-일:시)'].dt.day_name()
df['dayName']

#Q78 일자별 각 PM10등급의 빈도수를 파악하라
Ans1 = df.groupby(['dayName', 'PM10등급'], as_index=False).size()
Ans1
Ans2 = Ans1.pivot(index='dayName', columns='PM10등급', values='size').fillna(0)
Ans2

#Q79 시간이 연속적으로 존재하며 결측치가 없는지 확인하라
# 시간을 차분했을 경우 첫 값은 nan, 이후 모든 차분값이 동일하면 연속이라 판단한다.
check = len(df['(년-월-일:시)'].diff().unique())
if check == 2:
    Ans = True
else:
    Ans = False

Ans

#Q80 오전 10시와 오후 10시(22시)의 PM10의 평균값을 각각 구하여라
df.groupby(df['(년-월-일:시)'].dt.hour).mean().iloc[[10, 22], [0]]

#Q81 날짜 컬럼을 index로 만들어라
df.set_index('(년-월-일:시)', inplace = True, drop = True)
df

#Q82 데이터를 주단위로 뽑아서 최소,최대 평균, 표준표차를 구하여라
df.resample('W').agg(['min', 'max', 'mean', 'std'])

#06_Pivot
# 1개 그룹에 대한 단일 칼럼 결과
import pandas as pd
import seaborn as sns
df = sns.load_dataset('titanic')

df.pivot_table(index = 'who', values= 'survived')   # index에 그룹을 표기
df.pivot_table(columns = 'who', values = 'survived') # columns에 그룹을 표기

# 다중 그룹에 대한 단일 칼럼 결과
df.pivot_table(index=['who', 'pclass'], values='survived')

# index에 칼럼을 중첩하지 않고 행과 열로 펼친 결과
df.pivot_table(index='who', columns='pclass', values='survived')

#다중 통계함수 적용
df.pivot_table(index='who', columns='pclass', values='survived', aggfunc=['sum', 'mean'])

#연습문제
tips = sns.load_dataset('tips')
tips.head()

tips.pivot_table(index='smoker', columns='day', values='tip')
tips.pivot_table(index='day', columns='time', values='total_bill', aggfunc=['mean', 'sum'])

#Q83 Indicator을 삭제하고 First Tooltip 컬럼에서 신뢰구간에 해당하는 표현을 지워라
Dataurl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv'
df = pd.read_csv(Dataurl)
df

df.drop('Indicator', axis=1, inplace=True)
df['First Tooltip'] = df['First Tooltip'].map(lambda x: float(x.split("[")[0]))
df

#Q84 년도가 2015년 이상, Dim1이 Both sexes인 케이스만 추출하라
ans = df[(df.Period >= 2015) & (df.Dim1 == 'Both sexes')]

#Q85 84번 문제에서 추출한 데이터로
# 아래와 같이 나라에 따른 년도별 사망률을 데이터 프레임화 하라
ans.pivot_table(index='Location', columns='Period', values='First Tooltip')

#Q86 Dim1에 따른 년도별 사망비율의 평균을 구하라
df.pivot_table(index='Dim1', columns='Period', values='First Tooltip', aggfunc='mean').iloc[:,:4]

#Q87 데이터에서 한국 KOR 데이터만 추출하라
dataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv'
df = pd.read_csv(dataUrl)
df

Kor = df[df.Country == 'KOR']

#Q88 한국 올림픽 메달리스트 데이터에서 년도에 따른 medal 갯수를 데이터프레임화 하라
Kor.pivot_table(index='Year', columns='Medal', aggfunc='size').fillna(0)

#Q89 전체 데이터에서 sport종류에 따른 성별수를 구하여라
df.pivot_table(index='Sport', columns='Gender', aggfunc='size')

#Q90 전체 데이터에서 Discipline종류에 따른 따른 Medal수를 구하여라
df.pivot_table(index='Discipline', columns='Medal', aggfunc='size')


#07_Merge, Concat
"""
concat() : 2개 이상의 DataFrame을 행 혹은 열 방향으로 연결
merge() : 2개의 DataFrame을 특정 Key를 기준으로 병합할 때 활용
"""




Dataurl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv'
df = pd.read_csv(Dataurl)

#Q91 df1과 df2 데이터를 하나의 데이터 프레임으로 합쳐라
df1 = df.iloc[:4, :]
df2 = df.iloc[4:, :]

total = pd.concat([df1, df2])
total

#Q92 df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라.
# 둘다 포함하고 있는 년도에 대해서만 고려한다
df3 = df.iloc[:2,:4]
df4 = df.iloc[5:,3:]

total = pd.concat([df3, df4], join='inner')
total

#Q93 df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라.
# 모든 컬럼을 포함하고, 결측치는 0으로 대체한다
total = pd.concat([df3, df4], join='outer').fillna(0)
total

#Q94 df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라.
# Algeria컬럼을 key로 하고 두 데이터 모두 포함하는 데이터만 출력하라
df5 = df.T.iloc[:7,:3]
df6 = df.T.iloc[6:,2:5]

display(df5)
display(df6)

total = pd.merge(df5, df6, on='Algeria', how='inner')

#Q95 df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라.
# Algeria컬럼을 key로 하고 합집합으로 합쳐라
total = pd.merge(df5, df6, on='Algeria', how='outer')

