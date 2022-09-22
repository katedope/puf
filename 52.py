s = input()
p = []
q = []
for i in range(0, len(s)):
    q.append(s[i])
    if s[i] == '3':
        p.append(1)
    if s[i] == '4':
        p.append(1)
    if s[i] == '5':
        p.append(1)
print(q, sum(p), (sum(p)/len(s))*100)