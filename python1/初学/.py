flag = 1
while flag:
    a,b = input("请输入两个数字：(“,”隔开)").split(',')
    cal = input("请输入运算符：")
    if cal in "+-*/":
        if cal == '/':
            if b == '0':
                print("除数不能为0，请重新输入")
                continue
        s = eval(a+cal+b)
        print(s)
    else:
        print("输入不符合要求，请重新输入：")