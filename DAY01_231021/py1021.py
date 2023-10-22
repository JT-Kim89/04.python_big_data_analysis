#DAY01 오전
#코딩 실습

#무한루프
#while True:
#    print('무한루프')

#숫자형
a = 3
b = 4.5

#사칙연산
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a**b) #제곱
print(a%b) #나머지
print(a//b) # 몫

#문자열
a= '문자열'
b= "문자열"
c='아버지께서 "밥 먹어라!"라고 말씀하셨다.'
print(c)

#여러 줄인 문자열
c1='아버지께서 \n "밥 먹어라!" \n라고 말씀하셨다.' # 줄바꿈 \n
print(c1)

d= '''여러 줄1
여러 줄2
여러 줄3'''
print(d)

e= """  Add value
Inspire trust  """
print(e)

#문자열 인덱싱
len(e) #문자열 개수
print(e[0]) #문자열 인덱싱 0,1,2, ...(왼쪽에서 0번부터 시작)
print(e[-1]) #문자열 인덱싱 -1.-2,-3 ...(오른쪽에서 -1번부터 시작)

#문자열 슬라이싱
print(e[0:3]) # 0번이상 2번미만, 마지막 번호는 포함하지 않아서...
print(e[:3]) # 0번이상 생략가능, 2번까지
print(e[18:]) # 18번이상 마지막 번호까지

#문자열 관련 함수
e1 = e.upper() #대문자
print(e1)

e11 = e1.strip().lower() #공백 지우고, 소문자
print(e11)

e2 = e.count("u") # u개수
print(e2)

e3 = e.find("p")     # p 위치, 못찾으면 -1 출력
print(e3)


#DAY01. 오후 수업
#리스트
odd = [1, 3, 5, 7, 9]

#리스트의 인덱싱
a = []
a1 = list()
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

b[0]
b1 = b[1]+b[2]
print(b1)
e1 = e[2][0]
print(e1)

#중첩된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[2:5]
a[3][:2]

#리스트 반복하기
a1 = a * 3
print(a1)

#리스트 길이 구하기
len(a1) # 6 * 3 = 18

#리스트의 값 수정하기
a[3] = 0
print(a)

del a[3]
print(a)

#리스트에 요소 추가하기
a.append(6)
print(a)

#리스트 정렬 (내림차순)
a.sort()
print(a)

#리스트 뒤집기 (역순)
a.reverse()
print(a)

#인덱스 반환
a2 = a.index(3)

#리스트에 요소 삽입
a.insert(9,9)  # 6번 자리에 9 삽입
print(a)

#리스트 요소 제거
a.remove(0)  # 처음 나오는 0을 제거
print(a)

#리스트 요소 끄집어 내기
a3 = a.pop()   # 맨 마지막 요소를 리턴하고 그 요소는 삭제한다.
print(a)
print(a3)

#리스트에 포함된 요소 개수 세기 (중요)
a.count(1)

#리스트 확장
a.extend([11,10,14])
print(a)

a += [11,10,14]  #더하기만 됨
print(a)

#튜플 : 요소값을 지우거나 변경할 수 없음
t1 = ()
t2 = (1)
print(type(t2)) #정수로 인식함
t2 = (1,)
print(type(t2)) # 뒤에 콤마를 넣으면 튜플로 인식함
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b', ('ab', 'cd'))

t5[2][1]  #튜플 인덱싱

t3a = t3[0:1]  # 튜플 슬라이싱 -> 튜플 생성됨

t6 = t3 + t4 #튜플 더하기
t7 = t6 * 3 #튜플 곱하기
len(t7) #튜플 길이 구하기

#딕셔너리   {key1:Value1, Key2:Value2, ...}
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a = {1: 'hi'}
a = {'a': [1, 2, 3]}

#딕셔너리 쌍 추가하기
a[2] = 'b'
a
a['name'] = 'tom'
a
del a['a']
a

# Key를 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey']
grade['julliet']

# 주의사항  : Key가 중복으로 존재할 수 없다.
a = {1:'a', 1:'b'}
a

# Key 리스트 만들기
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.keys()

for k in a.keys():
    print(k)

list(a.keys())

a.values()  # Value 리스트 만들기
a.items()   # Key, Value 쌍 얻기
a.clear()   # Key: Value 쌍 모두 지우기

#Key로 Value 얻기
a.get('name')
a.get('phone')

#해당 key가 딕셔너리 안에 있는지 조사하기
'name' in a #있으면 True
'email' in a # 없으면 False

#집합 : 중복허용X, 순서X
s = set()
s1 = set([1, 2, 3])
s1
s2 = set("Hello")
s2

s1 = set([1, 2, 3, 3, 2, 1]) #리스트를 집합으로 변환
s1
l1 = list(s1) #집합을 리스트로 변환
l1

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
s1 & s2
s1.intersection(s2)

#합집합
s1 | s2
s1.union(s2)

#차집합
s1-s2
s1.difference(s2)

#값 1개 추가하기
s1.add(10)
s1

#값 여러 개 추가하기
s1.update([11,15,19])
s1

#특정 값 제거하기
s1.remove(3)
s1

# 불린: 조건이 맞는지 틀린지 판별
bool(1 == 1)    # 조건

bool('python') # 내용이 있으면 참
bool('')             # 비어있으면 거짓
bool(0)             # 0도 거짓
bool(None)     # None도 거짓

if []:
    print("참")
else:
    print("거짓")

#응용
a = [1,2,3]
while a:
    print(a.pop())

# IF문 : else 없이
money = 2000
if money >= 3000:
    print("택시를 탄다.")
print("집 도착")

# IF문 - else 포함
money = 2000
if money >= 3000:
    print("택시를 탄다.")
else:
    print("걸어 간다.")
print("집 도착")

# in, not in
1 in [1, 2, 3] # True
1 not in [1, 2, 3] # False

# IF문 - elif 포함
pocket = ['paper', 'cellphone']
card = True
if money in pocket:
    print("택시를 탄다.(현금 결제)")
elif card:
    print("택시를 탄다.(카드 결제)")
else:
    print("걸어 간다.")
print("집 도착")

