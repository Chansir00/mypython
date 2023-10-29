a = eval(input('请输入一个五位数数字'))
w = a // 10000
k = a // 1000 % 10
t = a // 10 % 10
g = a % 10
if w==g and k ==t :
    print(f'{a}是回文数')
else:
    print(f'{a}不是回文数')
