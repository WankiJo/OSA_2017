# r-읽을 때
# w-새로 쓸 때
# a-수정

f = open("C:/Users/rim/PycharmProjects/untitled/새파일.txt",'w')
data="새파일이 생성되었습니다."
f.write(data)
f.close()

f=open("C:/Users/rim/PycharmProjects/untitled/새파일.txt",'r')
line =f.readline() # 한줄씩 읽어오기
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f=open("C:/Users/rim/PycharmProjects/untitled/새파일.txt",'r')
data = f.read() # 전체읽기
print(data)
f.close()

f=open("C:/Users/rim/PycharmProjects/untitled/새파일.txt",'a')
for i in range(1, 6):
    data="\n%d번째 줄입니다." %i
    f.write(data)
f.close()