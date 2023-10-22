# 05-2 모듈
import Day2_03_func as func    #파일명이 숫자먼저 나오면 호출이 안됨
print(func.sub(10, 4))

from Day2_03_func import sub   # 특정 함수만 불러오는 경우
print(func.sub(10, 4))

from Day2_03_func import *   # 모든 함수를 불러오는 경우
print(func.sub(10, 4))


# 05-6 표준 라이브러리
import random
random.random()
help(random.random)
help(print)

