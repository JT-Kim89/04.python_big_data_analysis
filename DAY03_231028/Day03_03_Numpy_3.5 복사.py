# 3.5 복사
"""
Numpy의 ndarray와 대입연산자 = 를 사용하면 shallow copy가 되며,
실제복사(deep copy)하려면 object.copy()를 사용해야 한다.
"""
import numpy as np
a = [1,2,3]
x = np.array(a)
y = x       # shallow copy -> y를 변경하면 x까지 변경하게 된다.
y[0] = 10
a
x
y
y is x
z = x.copy()    # deep copy
z is x

# 3.8 기타
"""
nan(not a number) : 빈 공간으로 둠, 그림을 그릴 때 nan이 있으면 그 포인트는 그리지 않음
inf(infinite) : 무한대값, 비교시 초기값으로 활용하면 편리
"""
# nan
x = [1,2,3,4]
y1 = [4,7,,8,9]
y1
y2 = [4,7,np.nan,8,9]
y2

plt.plot(x,y1)
plt.plot(x,y2)

# inf
maximum = -np.inf
for x in data:
    if x > maximum:
        maximum = x