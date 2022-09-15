s = int(input())
a = int(input())
z = int(input())
if s<a and a<z:
    print('акция!', int((s+a+z)/2))
else:
    if s>a and a>z:
        print('акция!', int((s+a+z)/3))
    else: print(s+a+z)