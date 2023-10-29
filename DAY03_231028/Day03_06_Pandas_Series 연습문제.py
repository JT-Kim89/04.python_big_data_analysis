#Series 연습문제
import numpy as np
import pandas as pd

#1번
#a = np.arange(3, 13, 2)
a = np.linspace(3, 11, 5)
print(a)
s = pd.Series(a, dtype='float32')
print(s)

#2번
s = pd.Series(['가', '나', '다', '라', '마'])
print(s)

#3번
a = np.linspace(10, 50, 5)
print(a)
b= ['가', '나', '다', '라', '마']
sample = pd.Series(a, dtype='int64')
sample.index = b
print(sample)

#4번
sample[[1,3]]

#5번
np.random.seed(20)
sample2 = pd.Series(np.random.randint(100, 200, size=(15,)), dtype='int64')
sample2

sample2[sample2 <= 160]

#6번
sample3 = sample2[sample2 <= 160]
sample3[sample3 >= 130]


#7번
s = pd.Series(['apple', np.nan, 'banana', 'kiwi', 'gubong'])
s.index = b
print(s)

#8번
sample = pd.Series(['IT서비스', np.nan, '반도체', np.nan, '바이오', '자율주행'])
sample

sample[sample.isnull()]

#9번
sample[sample.notnull()]

#10번
np.random.seed(0)
sample = pd.Series(np.random.randint(100, 200, size=(10,)))
sample

sample[2:7]

#11번
np.random.seed(0)
sample2 = pd.Series(np.random.randint(100, 200, size=(10,)), index=list('가나다라마바사아자차'))
sample2

sample2['바':'차']

#12번
sample2['가':'다']

#13번
sample2['나':'바']



