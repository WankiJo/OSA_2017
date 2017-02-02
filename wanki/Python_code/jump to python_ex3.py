x=1
y=2
print(x>2)

money = 200
if money >= 300:
    print("택시를 탈것")
else:
    print("ㄴㄴ함")

card = 1
if money >= 300 or card:
    print("택시를 탈수 있어!")
else:
    print("걷기 ㄱㄱ")

print('a' in ('a','b','c'))

print('j' not in 'python')

pocket=['a','b','c']
if 'z' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어또")

if 'z' in pocket:
    pass
else:
    print("카드를 꺼내면 돼")

##while
treeHit = 0
while treeHit < 5:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 5:
        print("나무 넘어감 ㅋㅋ")

prompt ="""
1.Add
2.Del
3.List
4.Quit

Enter number:"""

number = 2
while number != 4:
    print(prompt)
    number = int(input())

#coffee.py
coffee = 3
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다" % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break


# for문 이해
test_list = ['1', '2', '3']
for i in test_list:
    print(i)

a= [(1,2), (3,4), (6,7)]
for ( first, last ) in a:
    print(first + last)

marks = [90, 23, 88]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

# range
sum = 0
for i in range(1,  11):
    sum = sum + i

print(sum)

# 복잡해 보이는 for문
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

# [표현식 for 항목 in 반복가능객체 if 조건]
result2 = [num*3 for num in a if num%2 ==0 ]
print(result2)

# 2개 이상 사용하기
result3 = [x*y for x in range(5,10)
               for y in range(8,10)]
print(result3)
