#03-2While

#while 문의 기본 구조
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

#while 문 만들기
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

#while 문 강제로 빠져나가기
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#coffe.py
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요:" ))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money-300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % (coffee))
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#while 문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)

#무한 루프
while True:
    print("stop console 버튼을 눌러야 while문을 빠져나갈 수 있습니다.")

#142-01
a = 0
while a <5:
    print("a값은 %s 입니다." % a)
    a += 1

print("while문이 종료되었습니다.")

#142-02
a = 0
b = ["사과","바나나","토마토"]
while a < len(b):
    print("바구니에서 %s를 꺼냈습니다" %b[a])
    a += 1

print("바구니에 아무것도 남아있지 않습니다.")


























