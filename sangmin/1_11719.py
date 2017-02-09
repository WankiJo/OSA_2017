import sys
text = ''
for i in sys.stdin:
    try:
        text += i
    except StopIteration:
        break

print(text)