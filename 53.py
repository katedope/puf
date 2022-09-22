s = input()
g = s.split()
d = 0
h = 0
for i in range(0, len(g)):
    h = h+1
    if g[i] == '5':
        d = d + 1
print((d*100)/h)