# 3.3 연산
import numpy as np

# 요소 단위 연산
a = np.array([1,2,3,4])
b = np.array([4,5,6,7])
a+b     # 요소별 더하기
a*b     # 요소별 곱하기
a**2    # 요소별 제곱
a+2     # 상수 2는 같은 크기의 배열로 인식
10*np.sin(a)    # Numpy의 universal 함수 sin() 적용
a<3
a *= b  # a = a * b 와 동일
a


# Universal 함수
x = np.arange(0., 2*np.pi, 0.1)
x
y = np.sin(x)
y


# 행렬 연산

A = np.arange(9).reshape(3,3)           # (3,3)
A
B = np.arange(11,11+9).reshape(3,3) # (3,3)
B

x = np.arange(3)                                # (3,)
x
y = np.arange(3).reshape(3,1)           # (3,1)
y
z = np.arange(3).reshape(1,3)           # (1,3)
z

# C = A * B ... same results (3,3) x (3,3)
C1 = np.dot(A, B)
C1
C2 = np.matmul(A, B)
C2
C3 = A@B
C3

# A * x ... 2d * 1d ... same results  (3,3) x (3,)
Ax1 = np.dot(A, x)    # array([5, 14, 23])
Ax1
Ax2 = np.matmul(A, x)
Ax3 = A@x

# A * y ... 2d * (2d, but 1d vector) ... same results   (3,3) x (3,1)
Ay1 = np.dot(A, y)      # array([[5],[14],[23]])
Ay1
Ay2 = np.matmul(A, y)
Ay3 = A@y

# A * z ... 2d * (2d, but 1d vector) ... all dimension error   (3,3) x (1,3) -> 행렬계산X
Az1 = np.dot(A, z)
Az2 = np.matmul(A, z)
Az3 = A@z

# left make (row vector), right make (column vector)
xy = x@y
xy


A.T                     #전치행렬
np.transpose(A)


A = np.array([[1,2,-1],[3,7,0],[0,4,-1]])
[D, V] = np.linalg.eig(A)   # D는 eigenvalues, V는 vector
D
V


# 정렬과 탐색
x = np.array([9.1,8.2,2.3,3,3,7.6,5.2])
np.amin(x)       # 최소값
np.argmin(x)    # 최소값 위치
np.sort(x)        # 정렬
np.argsort(x)   # 정렬 했을 때의 인덱스

imax2 = np.argsort(x)[-2]   # 두 번째로 큰 값의 위치
imax2



# 이진탐색 (binary search)
""" 
이미 정렬되어 있는 배열을 대상으로 탐색할 때, 계산효율 대폭 상승
"""
x = np.array([0., 3, 6, 13., 17, 22,  26., 30.])
x
np.searchsorted(x,13.)
np.searchsorted(x, 13., side='right')

# 216-01 넘파이 행렬 내적 계산
import numpy as np
array1 = np.array([[1,2,3],
                            [4,5,6]])
array2 = np.array([[7,8],
                            [9,10],
                            [11,12]])
dot_array = np.dot(array1,array2)   #  (2, 2) = (2, 3) * (3, 2)
print(dot_array)

# 216-02 넘파이 전치 행렬 계싼
transpose_array = np.transpose(array1)
print(transpose_array)

# 217-01 배열 데이터 개수 계산
x = np.array([18, 5, 10, 23, 19, -8,
              2, 5, 4, 15, -1, 4])
len(x)

# 217-02 평균, 분산, 표준편차
print(np.mean(x))
print(np.var(x))
print(np.std(x))

# 217-03 최대값, 최소값, 중앙값 계싼
print(np.max(x))
print(np.min(x))
print(np.median(x))

# 217-04 사분위수 계산
print(np.percentile(x,25))
print(np.percentile(x,50))
print(np.percentile(x,75))

print(np.mean(x))
print(np.median(x))
print(np.percentile(x,50))
