t = 0
while 1 > 0:
    s = int(input())
    while s != 0:
        t = t + s
    if s == 0: break
if t%2==0:
    while t%2==0:
        t = t/2
    print('к оплате', t)
else:
    print((t*(100-15)) /100)
