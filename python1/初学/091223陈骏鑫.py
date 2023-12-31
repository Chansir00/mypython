'''整体说明：1）共5道题，每题20分
             2）不允许修改函数名，严格按照题目要求答题，否则影响成绩后果自负。
             3）提交答卷之前，应进行充分测试，保证代码能够运行，确保没有语法错误。
             4）请将本测试文件另存为：班号+姓名，例如：191191张三.py
             '''


'''第一题：判断一个字符串是否为回文。如果参数s是回文则函数返回True，否则返回False。
           回文是指从前往后读和从后往前读都一样的字符串。
           提示：使用切片。'''
def one(s):
    # 删除下面的pass，然后编写自己的代码，完成题目要求的功能
    if s[::-1] == s[:]:
        return True
    else:
        return False



'''第二题：在下面的函数中，参数lst是一个包含若干（超过3）个整数的列表。
          要求：1）把列表中的元素升序排序；
                2）删除列表中最后一个元素；
                3）把列表中第一个元素移动到列表尾部；
                4）返回新列表。
          提示：使用列表方法，del语句或切片'''
def two(lst):
    # 删除下面的pass，然后编写自己的代码，完成题目要求的功能
    lst.sort()
    del lst[-1]
    a = lst[0]
    lst.append(a) 
    del lst[0]
    return lst
'''第三题：在下面的函数中，参数s1、s2、s3分别是3个集合，要求返回一个元组，
           元组中第一个元素是3个集合的并集，第二个元素是3个集合的交集，
           第三个元素是“s1与s2的并集”和“s2与s3的并集”的差集。
           提示：使用集合运算符。'''
def three(s1, s2, s3):
    # 删除下面的pass，然后编写自己的代码，完成题目要求的功能
    t = s1|s2|s3
    s = s1&s2&s3
    k = (s1|s2)-(s2|s3)
    tup  = (t,s,k)
    return tup

'''第四题：在下面的函数中，参数num是一个任意长度的自然数，要求返回各位数字的和。
           提示：使用内置函数sum()、map()和str()。'''
def four(num):
    # 删除下面的pass，然后编写自己的代码，完成题目要求的功能
    s = str(num)
    count = 0
    for i in s:
        count += eval(i)
    return count

'''第五题：在下面的函数one中，传入a、b两个列表，计算两个列表对应元素的乘积的累加和。
     如果列表长度不一致，则以较短的列表为主，忽略较长列表的其他元素。
     如列表a=[1,3,2]，列表b=[4,7,6,5]，则对应元素乘积的累加和为1*4+3*7+2*6=37。
     函数返回累加和。
     '''
def five(a,b):
    # 删除下面的pass，然后编写自己的代码，完成题目要求的功能
    c = 0
    if len(a) > len(b):
        for i in range(len(b)):
                c += a[i]*b[i]
    else:
        for i in range(len(a)):
                c += a[i]*b[i]
    return c



if __name__ == '__main__':
    # 下面是测试部分，根据前面的函数定义，自行设计测试数据，
    # 然后把下面函数调用中的下划线删除，替换为测试数据
    print(one("你好是好你"))
    print(two([3,5,2,1,6]))
    print(three({1,2,3,4},{3,4,5,6},{4,5,6,7}))
    print(four(4875))
    print(five([1,3,2,4,6],[4,7,6,5]))
