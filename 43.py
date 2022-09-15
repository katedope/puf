s = input()
r = '=?*^$№@'
for i in range(0, len(s)):
    for y in range(0, len(r)):
        if s[i]==r[y]:
            print('не верный символ:', s[i])