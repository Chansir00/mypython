a = 0
b = 1
n = int(input())
for i in range(n):
    if i == 0:
        a = 0
    else:
        a,b = b,a+b
    print(a)