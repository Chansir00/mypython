def hanoi(n,x,y,z):
    if n == 1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)
        print(x,'-->',z)
        hanoi(n-1,y,x,z)

n = int(input('请输入汉洛塔层数'))
hanoi(n,'A','B','C')
