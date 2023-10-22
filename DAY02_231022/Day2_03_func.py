# 04-1 함수

# 파이썬 함수의 구조
def add(a, b):          # a, b 는 매개변수(:함수에 입력으로 전달된 값을 받는 변수)
    return a+b           # 리턴값

a = 3
b = 4
c = add(a, b)           # add(3, 4)의 리턴값을 c에 대입
print(c)
print(add(3, 4))        # 3, 4는 인수(:함수를 호출할 때 전달하는 입력값)

# 입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)

# 리턴값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(3,4)
a = add(3,4)
print(a)

# 입력값도, 리턴값도 없는 함수
def say():
    print('Hi')

say()

# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)

result = sub(b=5, a=3)  #매개변수를 지정하면 순서에 상관없이 사용할 수 있는 것이 장점
print(result)

# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):    # 매개변수 앞에 별 1개(*)를 붙이면 입력값을 전부 모아 튜플로 생성
    result = 0
    for i in args:
        result += i         # *args에 입력받는 모든 값을 더한다.
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

# 키워드 매개변수, kwargs
def print_kwargs(**kwargs):     # 키워드 매개변수를 사용할 경우 별 2개(**)를 붙임.
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

