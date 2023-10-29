from functools import reduce
s = 0
for n in range(1,21):
    a = reduce(lambda x,i: x*i ,[i for i in range(1,n+1)])
    s += a
print(s)


