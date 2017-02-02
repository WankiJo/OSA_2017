money=20000
card=1
if money >= 3000 or card:
    print("택시타고 가라")
else:
    print("걸어가라")

pocket=['paper','phone','money']
if 'money' in pocket:
    print("택시타고 가라")
else:
    print("걸어가라")


if 'money' in pocket:
    print('택시')
elif card:
    print("택시")
else:
    print("걸어가라")
    