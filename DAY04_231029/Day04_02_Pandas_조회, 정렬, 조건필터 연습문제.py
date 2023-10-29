# 조회, 정렬, 조건필터 연습문제
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

# 1번문제
df.value_counts("embark_town")

# 2번문제
df.value_counts("who")

#3번문제
tips = sns.load_dataset('tips')
tips.head()

tips.sort_values(by=['total_bill','tip'], ascending=False).head(10)

#4번문제
tips.sort_values(by=['size','tip'], ascending=[False,True]).head(10)


#5번문제
df.iloc[3:8]

#6번문제
df.loc[0:5 ,['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare']]

#7번문제
df.loc[2:10:2, ['age', 'who']]


#8번문제
df = sns.load_dataset("titanic")
df.head()

cond1 = (df['age'] >= 30)
cond2 = (df['sex'] == 'male')
df.loc[cond1 & cond2].sort_values(by=['fare'], ascending=False).head(10)

#9번문제
cond3 = (df['age'] >= 20)
cond4 = (df['age'] < 40)
cond5 = (cond3 & cond4)

cond6 = (df['pclass'] == 1)
cond7 = (df['pclass'] == 2)
cond8 = (cond6 | cond7)

index = ('survived', 'pclass', 'age', 'fare')

df.loc[cond5 & cond8, index].head(10)


#10번문제
tips = sns.load_dataset('tips')
tips.head()

condi9 = (tips['day'] == "Fri")
condi10 = (tips['day'] == "Sat")
condi11 = (condi9 | condi10)

condi12 = (tips['tip'] < 10)

index2 = ('total_bill', 'tip', 'smoker', 'time')

tips.loc[condi11 & condi12, index2].head(10)

#10번 문제 해설
tips.loc[tips['day'].isin(['Fri','Sat'])&(tips['tip']<10), ['total_bill', 'tip', 'smoker', 'time']].head(10)