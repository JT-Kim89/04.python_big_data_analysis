#3.1 ndarray
"""
Numpy의 핵심은 ndarray 객체이다.
ndarray : fixed-size homogeneous multidimensional array
 - vectorization, braodcasting 지원
 - 성능향상을 위해 같은 데이터타입만을 요소로 가질 수 있고, 크기가 고정됨.

"""

import numpy as np
x = np.array((0.1,0.2,0.3))    # np.array([0.1,0.2,0.3])도 가능
x
type(x)     # 튜플X, 배열

x.shape     #배열의 형태, 1차원 배열 (1X3)
x.dtype     # 데이터 타입, 성능향상을 위해 같은 데이터타입만 요소로 가질 수 있음.

y = np.array(((1, 2, 3), (4, 5, 6)))
y
y.shape     # 2차원 배열 (2X3)
y.dtype     # 32비트 정수

z = np.array([1,2,3],dtype='float64')  # 64비트 실수로 미리 정의



# 초기화 관련 편의함수
X = np.zeros((3,3))     # 3x3 배열 모두 0으로 생성
X
Y = np.ones((3,3),dtype='int32')    # 3x3 배열 모두 1로 생성
Y
Z = np.empty((3,3))     # 값을 초기화하지 않고 생성 (메모리 상태에 따라 다른 값이 들어감)
Z

# 크기를 지정하지 않고 순차적으로 만드는 경우, 0배열 생성 후 append() 수행
A = np.array([])
for i in range(3):
    A = np.append(A, [1,2,3])   # A배열에 [1, 2, 3]을 추가함

help(np.append)

A

np.arange(1,2,0.1)         # arange(from, to, step) 1부터 2까지 0.1 간격으로 생성
np.arange(10)                # 0 ~ 9 정수로 생성
np.arange(10.)               # 0 ~ 9 실수로 생성
np.linspace(0., 20., 11)   # (linspace(from, to, npoints) 0부터 20까지 11개 등간격으로 생성
np.eye(3)                       # 단위행렬



# shape과 dtype 변경
X = np.arange(0,9,1.)
X
Y = np.reshape(X, (3,3))    # 1차원 1x9 -> 2차원 3x3로 변환
Y

X.shape = (3,3)                 # 자기 자신을 대상을 변경하면 shape 속성을 강제로 변경하면 된다.
X

a = np.arange(3);
a.astype(int)           # a.astype('int32')와 동일
a.astype('int32')
a.astype('int64')
a.astype(float)           # a.astype('float64')와 동일
a.astype('float32')
a.astype('float64')

