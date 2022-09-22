e = int(input()) # количество преподователей
p=[]
h = []
l = 0
for i in range(0, e):
    l = l + 1
    p.append(l)

for y in range(0, len(p)):
    p[y] = []
    f = input('фамилия')
    p[y].append(f)
    d = input('должность')
    p[y].append(d)
    k = input('кол-во студентов')
    p[y].append(k)
    h.append(p[y])

print(h)






