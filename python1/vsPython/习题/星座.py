f = open("PY301-SunSign.csv",'r')
ls = []
flag = True
x = input("请输入星座序号（例如，5）：")
num = x.split()
for i in num:
    if 1<= eval(i) <= 12:
        li = f.readlines()[eval(i)+1]
        print("{}({})的生日是{}月{}日至{}月{}日之间".format(li[1],li[4],li[2][:-2].li[2][-2:],li[3][:-2],li[3][-2:]))
    else:
        print("输入星座序号有误！")
        x = input("请输入星座序号（例如，5）：")