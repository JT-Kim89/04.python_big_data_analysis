# 3.4 브로드캐스팅
# Broadcasting : 차원이 맞지 않는 객체끼리 연산이 되도록 하는 것

import numpy as np
A = np.arange(9.).reshape(3,3)  # 2d array : (3,3)
x = np.array([1.,0,0])                  # 1d array : (3,)
y = x.reshape(1,3)                      # 2d array : (1,3)
z = x.reshape(3,1)                      # 2d array : (3,1)
A
x
y
z

A+1             # (3,3) + scalar ==> (3,3) + scalar * I

# (3,3) + (3,) ==> (3,3)
"""
x = [1,0,0] --> expand with (3,3)
0 1 2     1 0 0 
3 4 5  + 1 0 0
6 7 8     1 0 0 
"""
A + x

# (3,3) + (1,3) ==> (3,3)
"""
y = [[1,0,0]] --> expand with (3,3)
0 1 2     1 0 0 
3 4 5  + 1 0 0
6 7 8     1 0 0 
"""
A + y

# (3,3) + (3,1) ==> (3,3)
"""
z = [[1],[0],[0]] --> expand with (3,3)
0 1 2     1 1 1 
3 4 5  + 0 0 0
6 7 8     0 0 0 
"""
A + z

# (1,3) + (3,1) ==> (3,3)
"""
each dimensions are expanded with (3,3)
1 0 0     1 1 1 
1 0 0  + 0 0 0
1 0 0     0 0 0 
"""
y + z


# 행렬 연산 함수 호출시 주의사항
A = np.arange(9.).reshape(3,3)      # (3,3) 2d array
x = np.array([2,0,1])                       # (3, ) 1d array
y = x.reshape(1,3)                          # (1,3) 2d array
z = x.reshape(3,1)                          # (3,1) 2d array
A
x
y
z

np.matmul(A,y)      # (3,3) * (1,3) -> Dimension Error
np.matmul(A,z)      # (3,3) * (3,1) -> (3,1)

np.matmul(A,x)      # (3,3) * (3, ) -> (3,)




