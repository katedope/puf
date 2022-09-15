s = int(input())
f = s
r = 0
while f > 1:
    f = f/10
    r = r+1
w = 0
k = 10
l = 100
o = s % 10
while w <= r:
    w = w + 1
    h = (s % l - s % k)/k
    o = o + h
    k = 10 * k
    l = 10 * l
d = s % 10
if d % 2 == 0 and o % 3 == 0:
    print('делиться на 6')
else:print('не делиться на 6')

