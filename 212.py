s = input()
i = 0
r = '0123456789'
p = 0
for i in range(0, len(s)):
    for p in range(0, len(r)):
        if s[i] == r[p]:
            a = s[i]
            print(end=a)

