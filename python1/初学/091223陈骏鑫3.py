'''整体说明：1）共5道题，每题20分
             2）不允许修改函数名，严格按照题目要求答题，否则影响成绩后果自负。
             3）提交答卷之前，应进行充分测试，保证代码能够运行，确保没有语法错误。
             4）请将本测试文件另存为：班号+姓名，例如：191191张三.py
             '''


'''第1题： 编写函数，接收字符串参数，返回一个元组，该元组中第一个元素为大写字母个数，
第二个元素为小写字母个数。
     '''
def one(s):
    l = 0
    x = 0
    for i in s:
        if i.islower():
            x += 1
        else:
            l += 1
    return(l,x)


'''第2题： 编写函数计算任意位数的黑洞数。问题描述：黑洞数是指这样的整数，
   即由这个数字每位上的数字组成的最大数减去每位数字组成的最小数仍然得到这个数本身。
   例如：3位黑洞数是：495，因为954-459=495；4位黑洞数是6174，因为7641-1467=6174，
   编写函数，参数n，表示数字的位数，例如：n=3时，返回495，n=4时，返回6174.'''
def two(n):
    x = 10**n
    y = 10**(n-1)
    for i in range(y,x):
        ls = list(map(str,str(i)))
        ls.sort()
        list_min = ls[:]
        while list_min[0] == '0':
            del list_min[0]

        ls.sort(reverse=True)
        list_max = ls[:]
        min= eval(''.join(list_min))
        max = eval(''.join(list_max))
        if max - min == i:
            return i

    
        


'''第3题：编写函数，寻找给定序列中相差最小的两个数字。以元组形式返回这两个数字。
   例如：输入：[12,15 ,6,26,8,88],返回：（6,8）
     '''
def three(seq):
    ls = []
    for i in seq:
        for j in seq:
            if i!=j:
                ls.append(abs(i-j))
    ls.sort()
    # print(ls)
    seq.sort()
    for i in seq:
        for j in seq:
            if i!= j:
                if abs(i-j) == ls[0]:
                    return (i,j)


'''第4题：编写函数，计算字符串匹配的准确率。
以打字练习程序为例，假设origin为原始内容，userInput为用户输入的内容，函数用来测试用户输入的准确率。
准确率作为函数值返回。
    '''
def four(origin,userInput):
    count = 0
    for i in range(len(origin)):
        if origin[i] == userInput[i]:
            count += 1
    
    if len(origin) != len(userInput):
        return '字符串长度不同，请重新输入'
    
    return "{:%}".format(count/len(origin))


'''第5题：编写函数，实现辗转相除法。接收两个整数，返回这两个整数的最大公约数。

 '''
def five(m,n):
    if m < n:
        x = m
        m = n
        n = x
    while m%n != 0:
        temp = m%n
        m = n
        n = temp
    return n

if __name__ == '__main__':
    # 下面是测试部分，根据前面的函数定义，自行设计测试数据，
    # 然后把下面函数调用中的下划线删除，替换为测试数据
    print(one('ADvjksF'))
    print(two(4))
    print(three([12,15 ,6,26,8,88]))
    print(four('打字练习程序为例','打字为人程序为例'))
    print(five(64,96))
    
    
