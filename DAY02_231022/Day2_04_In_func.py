# 05-5 내장함수

abs(-3) # 절대값
all([1, 2, 3]) # 모두 참이면 True, 하나라도 거짓이면 False
any([1,2,3,0]) # 하나라도 참이면 True, 모두 거짓이면 False
chr(44032) #유니코드 숫자값을 받아 문자 리턴
dir([1, 2, 3]) # 객체가 지닌 변수나 함수를 보여주는 함수
divmod(7,3) # a를 b로 나눈 몫과 나머지를 튜플로 리턴
for i, name in enumerate(['body', 'foo', 'bar']): #리스트, 튜플, 문자열을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴 (주로 for문과 함께 사용)
    print(i, name)
eval('1+2') # 문자열로 구성된 표현식을 입력받아 실행한 결과값 리턴

# Filter

#positive.py
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print (positive([1,-3,2,0,-5,6]))

#filter1.py
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))

hex(234) #16진수 변환

int('3')
int(2.5) # bankers rounding 적용
int('1101',2) # 2진수 -> 10진수
int('2A',16) # 16진수 -> 10진수

len('python') #문자열 개수
len([1,2,3]) #리스트 내 요소 개수

list('python') #문자열 하나씩 list화
list((1,2,3)) #튜플을 list로 변경


pow(2,4) # x를 y제곱한 결과값 리턴
pow(2, 1/2)

round(3.1415926, 2)

sorted([3,1,2]) # 정렬, 오름차순
str(3) # 문자열로 변환

sum([3,1,2]) # 합을 리턴

list(zip([1,2,3],[4,5,6]))





