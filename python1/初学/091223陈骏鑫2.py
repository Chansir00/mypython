'''整体说明：1）共5道题，每题20分
             2）不允许修改函数名，严格按照题目要求答题，否则影响成绩后果自负。
             3）提交答卷之前，应进行充分测试，保证代码能够运行，确保没有语法错误。
             4）请将本测试文件另存为：班号+姓名，例如：191191张三.py
             '''
'''第1题：使用多分支选择结构将成绩从百分制变换到等级制。

      在下面的函数one中，传入一个0—100的课程成绩数，变换到对应的等级制。作为函数值返回。
      score > 100 or score < 0: 返回：'WRONG'
      90<=score <=100:          返回： 'A'
      80<=score <90:            返回： 'B'
      70<=score <80:            返回： 'C'
      60<=score <70:            返回： 'D'
      score<60                  返回： 'E'
     '''

def one(score):
    if score > 100 or score < 0 : return 'WRONG'
    elif  90<=score <=100:          return 'A'
    elif  80<=score <90:            return 'B'
    elif  70<=score <80:            return 'C'
    elif  60<=score <70:            return 'D'
    elif  score<60  :               return 'E'


'''第2题：中国南北朝时期（公元5世纪）的数学著作《孙子算经》卷下第二十六题，叫做“物不知数”问题，
原文如下：“有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二。问物几何？”。
即，一个整数除以三余二，除以五余三，除以七余二，求这个整数是多少？
   在下面的函数two中，实现改功能，返回10000以为符合该条件的整数，放在列表中返回。
     '''
def two():
    ls = []
    for i in range(10001):
        if i % 3 ==2 and i % 5 == 3 and i % 7 == 2:
            ls.append(i)
    return ls

'''第3题：有1、2、3、4共四个数字，能组成多少个互不相同且无重复的三位数？
     在下面的函数three中，实现该功能，返回两个值，一个是这些数组成的列表,一个是这些数的数目。
     例如：([123, 124, 132, 134, 142, 143, 213, 214, 231, 234, .......], 24)
     '''
def three():
    li = []
    ls = [1,2,3,4]
    for i in ls:
        for j in ls:
            for k in ls:
                if i!= k and i!=j and j!=k:
                    li.append(i*100 + j*10 +k)
    return li,len(li)

'''第4题：对于任意一个1000以内的正整数，编写函数实现因子分解，并返回。
   在下面的函数four中，实现该功能，返回两个值，第一个是该数，第二个是该数的因子组成的列表。
     例如：函数传入90，则函数返回：(90，[2,3,3,5])

    '''
def four(x):
    ls = []
    i = 2
    while i <= x:
        if x % i == 0:
            ls.append(i)
            x = x / i
        else:
            i += 1
    return ls


'''第5题：函数five传入两个参数输入身高(米)h和体重(公斤)h.
    根据BMI公式计算BMI指数：计算公式为：BMI=体重÷身高²。（体重单位：千克；身高单位：米。）
    1、世界卫生组织，WHO 标准:
               bmi < 18.5:       WHO = "偏瘦"
            18.5 <= bmi < 25	 WHO = "正常"
            25 <= bmi < 30	 WHO = "偏胖"
                bmi >=30 	 WHO = "肥胖"
   2、我国卫生部标准DOM标准:
            bmi < 18.5: 	DOM = "偏瘦"
        18.5 <= bmi < 24	DOM = "正常"
         24 <= bmi < 28	        DOM = "偏胖"
            bmi >=28	        DOM = "肥胖"
    函数返回两个不同的标准值：国际标准WHO值，和国内标准DOM值。作为元组返回。
     '''
def five(h,w):
    # 删除下面的pass，然后编写自己的代码，完成题目要求的功能
    ls1 = [0,18.5,25,30]
    ls2 = [0,18.5,24,28]
    value = ['偏瘦','正常','偏胖','肥胖']
    bmi = w/h**2
    for i in range(len(ls1)):
        if bmi > ls1[i]:
            WHO = value[i]
    for i in range(len(ls2)):
        if bmi > ls2[i]:
            DOM = value[i]
    return (WHO,DOM)
    

if __name__ == '__main__':
    # 下面是测试部分，根据前面的函数定义，自行设计测试数据，
    # 然后把下面函数调用中的下划线删除，替换为测试数据
    print(one(99))
    print(two())
    print(three())
    print(four(90))
    print(five(1.75,75))
    
    
