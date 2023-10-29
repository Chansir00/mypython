jl = [[],[],[],[],[]]   # 1:zb_h, zb_l,yb_h,yb_l
zyc = []
yyc = []
with open("xueyajilu.txt", 'r',encoding='utf-8') as fi:
    for l in fi:
        if len(l):
            lls = l.split(',')
            for i in range(1,5):
                jl[i].append(eval(lls[i]))
            zyc.append(eval(lls[1])- eval(lls[2]))
            yyc.append(eval(lls[3])- eval(lls[4]))
cnt = len(zyc)
res = []
res.append(list(("高压最大值",max(jl[1]),max(jl[3]))))
res.append(list(("低压最大值", max(jl[2]),max(jl[4]))))
res.append(list(("压差平均值", sum(zyc)//cnt,sum(yyc)//cnt)))
res.append(list(("高压平均值", sum(jl[1])//cnt,sum(jl[3])//cnt)))
res.append(list(("低压平均值", sum(jl[2])//cnt,sum(jl[4])//cnt)))
print("{0:<10}{1:<10}{2:<10}".format("对比项","左臂","右臂"))
for r in range(len(res)):
    print("{0:<10}{1:<10}{2:<10}".format(res[r][0],res[r][1],res[r][2]))