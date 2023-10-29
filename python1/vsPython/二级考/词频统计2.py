import jieba
with open("sgld.txt","r",encoding ="utf-8") as f:
    lssgld = f.readlines()
    
d = {}
for l in lssgld:
    for c in "，。：“” \n":
        l = l.replace(c,"")
    wd = jieba.cut(l)
    for i in wd:
        d[i] = d.get(i,0) + 1
ls = list(d.items())                              #要理解这行代码
ls.sort(key=lambda x:x[1], reverse = True)        #要理解这行代码
for s in range(5):
    print("{}".format(ls[s][0]),end='、')