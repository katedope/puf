a = int(input())
s = a % 10
z = a % 100 - s
d = (a % 1000 - s-z)/100
print(int((s+z/10)+d))
