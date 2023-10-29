import seaborn as sns
import pandas   as pd

#1번문제
df = sns.load_dataset('titanic')
df.head()

df1 = df.copy()

drop_index = [1,3,5]
drop_list = ['embarked', 'class', 'alone']
df1.drop(drop_index).drop(drop_list, axis=1).head(10)

#2번문제
iris = sns.load_dataset('iris')
iris.head()

iris['sepal'] = iris['sepal_length'] * iris['sepal_width']
iris.head(5)

#3번문제
iris['petal'] = iris['petal_length'] * iris['petal_width']
iris.head(5)

#4번문제
remove_list = ['petal_length', 'petal_width']
iris.drop(remove_list, axis=1).head(5)

#5번문제
cond1 = iris['species'] == "setosa"
iris.loc[cond1].sort_values(by="sepal", ascending=False).head(10)

#6번문제
iris['sepal'].mean() - iris['petal'].mean()

#7번문제
df2 = pd.read_csv('data/서울시자전거/seoul_bicycle.csv')
df2.head()
df2.info()
df2["대여일자"] = pd.to_datetime(df2["대여일자"])





