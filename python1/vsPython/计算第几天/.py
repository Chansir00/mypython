def count():
    year =int(input('请输入年份'))
    month = int(input('请输入月份'))
    bigm = [1,3,5,7,8,10,12]
    smam = [4,6,9,11]
    day = int(input('请输入日期'))
    if month in bigm:
        c = month * 31 + day
    elif month in smam:
        c = month * 30 + day
    else:
        if year % 4 == 0 and year % 100 != 0:
            c = month * 29 + day
        else:
            c = month * 28 + day
    print(c)  

count()