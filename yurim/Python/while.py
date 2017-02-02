
treeHit =0
while treeHit < 5:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 5:
        print("나무 넘어갑니다")

coffee = 10
money=300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee=coffee-1
    print("남은 커피의 양은 %d개입니다." %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다.")
        break # while문 빠져나감 #없으면 커피 -1개가 되며 무한루프가 됨

a=0
while a<10:
    a=a+1
    if a%2==0:continue # 다음문장은 실행하지않고 while문을 실행한다
    print(a)