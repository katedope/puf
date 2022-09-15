o = 1
while o > 0:
    p = input()
    if p == 'off':
        break
    else:
        if p == 'game':
            for i in range(3):
                f = int(input())
                if f == 5:
                    print('win')
                else:
                    print('в другой раз, сыграем еще?')
            else:
                print('нет такой игры')






