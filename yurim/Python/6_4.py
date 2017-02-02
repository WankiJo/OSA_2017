def readMemo():
    f=open("C:/Users/rim/PycharmProjects/untitled/memo.txt",'r')
    data=f.read()
    print(data)
    f.close()

def addMemo():
    f = open("C:/Users/rim/PycharmProjects/untitled/새파일.txt", 'a')
    data=input()
    f.write(data)
    f.close()
    