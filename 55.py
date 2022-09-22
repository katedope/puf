s = input()
s.split()
t = int(s[1]) - int(s[0])
for i in range(0, len(s)):
    for u in range(1, len(s)):
        if int(s[u]) - int(s[i]) == t:
            p = 'tru'
        else: p = 0