# import sys
# a = sys.stdin.readlines()
#
# print(a)
# text = ''
# for i in range(0, 100):
#     a = input() + '\n'
#     text += a
#
# print(text)

import sys
text = ''
for i in sys.stdin:
    try:
        text += i
    except StopIteration:
        break

print(text)