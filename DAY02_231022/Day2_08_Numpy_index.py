# 3.2 인덱싱과 합치기
import numpy as np

#인덱싱
a = np.array([1.2, -1.3, 2.2, 5.3, 3.7])
a[0]
a[0:3]
a[-1]
a[0:-1]

# 인덱스 배열
idx = [0,3]  # 0번, 3번 인덱스 지정
a[idx]         #  지정된 인덱스 배열 생성

# 불린 배열 (PASS)

# 합치기
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
np.concatenate((a,b),axis=0)     # 행에 추가
np.concatenate((a,b.T),axis=1)  # .T 는 transpose -> 행렬 계산을 위해 전치, 열에 추가

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.vstack((a,b))   # 같은 크기(1x3) 배열의 높이방향으로 누적 -> (2x3)
np.hstack((a,b))   # 같은 크기(1x3) 배열의 길이방향으로 누적 -> (1x6)

c = np.append(a,b)  # hstack과 동일?
c

