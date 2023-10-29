# Concat, Merge
import pandas as pd
from opendata import dataset

# 유가정보 데이터 다운로드
dataset.download('유가정보')

gas1 = pd.read_csv('data/유가정보/gas_first_2019.csv', encoding='euc-kr')
print(gas1.shape)
gas1.head()

gas2 = pd.read_csv('data/유가정보/gas_second_2019.csv', encoding='euc-kr')
print(gas2.shape)
gas2.head()

# Concat() - 데이터 연결
#행 방향으로 연결

pd.concat([gas1, gas2])     # 같은 칼럼을 알아서 찾아서 데이터 연결
pd.concat([gas1, gas2]).iloc[90588:90593]       # 연결시 index 초기화 되지 않음

gas = pd.concat([gas1, gas2], ignore_index=True)    # index를 무시하고 연결
gas

gas11 = gas1[['지역', '주소', '상호', '상표', '휘발유']]
gas22 = gas2[['상표', '번호', '지역', '상호', '주소', '경유', '휘발유']]

gas11.head()
gas22.head()

pd.concat([gas11, gas22], ignore_index=True)


# 열 방향으로 연결
gas1 = gas.iloc[:, :5]
gas2 = gas.iloc[:, 5:]
gas1.head()
gas2.head()

pd.concat([gas1, gas2], axis=1)


# Merge() - 병합
# 서로 다른 구성의 DataFrame이지만, 공통된 Key값을 가지고 있다면 병합할 수 있음.

df1 = pd.DataFrame({
    '고객명': ['박세리', '이대호', '손흥민', '김연아', '마이클조던'],
    '생년월일': ['1980-01-02', '1982-02-22', '1993-06-12', '1988-10-16', '1970-03-03'],
    '성별': ['여자', '남자', '남자', '여자', '남자']})
df1

df2 = pd.DataFrame({
    '고객명': ['김연아', '박세리', '손흥민', '이대호', '타이거우즈'],
    '연봉': ['2000원', '3000원', '1500원', '2500원', '3500원']})
df2


# 병합하는 방법 4가지
# how : left, right, outer, inner(default)

pd.merge(df1, df2)
pd.merge(df1, df2, how='left')
pd.merge(df1, df2, how='right')
pd.merge(df1, df2, how='outer')

# 병합하려는 칼럼의 이름이 다른 경우
df1 = pd.DataFrame({
    '이름': ['박세리', '이대호', '손흥민', '김연아', '마이클조던'],
    '생년월일': ['1980-01-02', '1982-02-22', '1993-06-12', '1988-10-16', '1970-03-03'],
    '성별': ['여자', '남자', '남자', '여자', '남자']})
df1

df2 = pd.DataFrame({
    '고객명': ['김연아', '박세리', '손흥민', '이대호', '타이거우즈'],
    '연봉': ['2000원', '3000원', '1500원', '2500원', '3500원']})
df2

pd.merge(df1, df2, left_on='이름', right_on='고객명')    # drop되지 않을 칼럼 지정