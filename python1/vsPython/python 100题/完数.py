ls = []
for i in range(1000):
    li = []
    for j in range(2,i+1):
        if i%j == 0:
            li.append(j)
            i -= j
s = 0
for each in li:
    s += each
    if s == i:
        ls.append(i)

print(ls)
