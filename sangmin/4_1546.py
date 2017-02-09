a = int(input())
score = list(map(int, input().split(" ")))

max = max(score)
avg = 0

for i in range(0, a):
    score[i] = score[i] / max * 100
    avg += score[i]

avg /= a
# print(round(avg, 2)) 75.0은 안되고 75.00이 정답이 됨. 망할
print("%.2f" % round(avg, 2))