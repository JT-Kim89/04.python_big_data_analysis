#3.1 ndarray
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

np.arange(1,2,0.1)
np.arange(10)
np.arange(10.)
np.linspace(0., 20., 11)
np.eye(3)

# shape과 dtype 변경
X = np.arange(0,9,1.)
X
Y = np.reshape(X, (3,3))    # 1차원 1x9 -> 2차원 3x3로 변환
Y

X.shape = (3,3)
X

a = np.arange(3);
a.astype(int)
a.astype('int32')
a.astype('int64')
a.astype(float)
a.astype('float32')
a.astype('float64')

