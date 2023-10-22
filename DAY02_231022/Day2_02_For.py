#03-3 for문

#예제를 통해 for 문 이해하기
#1. 전형적인 for 문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#2. 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:   # 1번에 2개씩 불러오는 경우
    print(first + last)

#3. for 문의 응용
# mark1.py
marks = [90, 25, 67, 45, 80]  #학생들의 시험 점수 리스트

number = 0      # 학생에게 붙여 줄 번호
for mark in marks:      # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# for 문과 continue문
# marks2.py
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue        # for문의 처음으로 돌아감.
    print("%d번 학생 축하합니다. 합격입니다." % number)

# for 문과 함께 자주 사용하는 range 함수 (함수가 아니라 사실 클래스임)
a = range(10)    # 끝_숫자
a                       # range 객체 생성됨

a = range(1,11)  # 시작_숫자, 끝_숫자
a

# range 함수의 예시 살펴보기
add = 0
for i in range(1,11):
    add += i

print(add)

# mark3.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

#for와 range를 이용한 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end="  ")   # end 파라미터를 설정하여 다음 줄로 넘기지 않고 그 줄에 계속 출력
    print(' ')   # 2단, 3단 구분하기 위해 사용

#리스트 컴프리헨션(list comprehension
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2,10)
                   for y in range(1,10)]
print(result)


#143-01
a = ["사과", "바나나", "토마토"]
for i in a:
    print(i)

#143-02
a = [90, 25, 67, 45, 80]
b = sum(a) / len(a)

for i in a:
    if i > b:
        print("%d 는(은) 평균보다 크다" % i)
    else:
        print("%d 는(은) 평균보다 작거나 같다" % i)






