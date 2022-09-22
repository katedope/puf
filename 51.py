f=1
e = []
while f != '0':
    s = input()
    if s != '0':
        if s in e:
            print('эта игра уже есть')
        else: e.append(s)
    else: break
print(sorted(e))


