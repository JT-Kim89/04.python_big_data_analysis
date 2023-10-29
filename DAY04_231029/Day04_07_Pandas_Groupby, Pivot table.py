# Groupby와 Pivot table
import pandas as pd
import seaborn as sns
df = sns.load_dataset('titanic')
df.head()

# apply() - 함수 적용
df['who'].value_counts()

# 함수(function) 정의
def transform_who(x):
    if x == "man":
        return '남자'
    elif x == "woman":
        return '여자'
    else:
        return '아이'

df['who'].apply(transform_who)

df['who'].apply(transform_who).value_counts()

def transform_who(x):
    return x['fare'] / x['age']

df.apply(transform_who, axis=1)

# apply() - lambda 함수 : 간단한 logic은 함수를 정의하지 않고, lambda 함수로 해결
df['survived'].value_counts()
df['survived'].apply(lambda x: '생존' if x == 1 else '사망')
df['survived'].apply(lambda x: '생존' if x == 1 else '사망').value_counts()


# Groupby()
df.groupby('sex').mean()

#2개 이상의 칼럼으로 그룹
df.groupby(['sex', 'pclass']).mean()

#1개의 특정 칼럼에 대한 결과 도출
df.groupby(['sex', 'pclass'])['survived'].mean()

# DataFrame으로 출력
pd.DataFrame(df.groupby(['sex', 'pclass'])['survived'].mean())

df.groupby(['sex', 'pclass'])[['survived']].mean()

# reset_index() : 인덱스 초기화
# 그룹핑된 데이터프레임의 index를 초기화하여 새로운 데이터프레임을 생성

df.groupby(['sex', 'pclass'])['survived'].mean().reset_index()

# 다중 칼럼에 대한 결과 도출
df.groupby(['sex', 'pclass'])[['survived', 'age']].mean()

# 다중 통계 함수 적용
df.groupby(['sex', 'pclass'])[['survived', 'age']].agg(['mean', 'sum'])


#연습문제
#1번
sample = df.copy()
sample['class'].value_counts()

# 함수
def transform_class(x):
    if x == "First":
        return "일등석"
    elif x == "Second":
        return "이등석"
    else:
        return "삼등석"

sample['class'].apply(transform_class)
sample['class'].apply(transform_class).value_counts()

#2번
sample = df.copy()
sample.groupby('pclass')['survived'].mean()

#3번
sample.groupby('embarked')['survived'].agg(['mean', 'var'])

#4번
sample.groupby(['who', 'pclass'])['survived'].agg(['mean', 'sum'])

#5번
#결측치 확인
print(sample['age'].isnull().sum())
print(f"age 평균: {sample['age'].mean():.2f}")

sample.head()
cond1 = sample['sex'] == 'male'
mean2 = sample.loc[cond1]['age'].mean()
sample.loc[cond1]['age'].fillna(mean2, inplace=True)
sample.loc[cond1]['age']

