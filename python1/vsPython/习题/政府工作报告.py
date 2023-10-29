import jieba
def getwords(fl):
    d = {}
    f = open(fl,'r')
    for lines in f.readlines():
        lines = lines.replace('\n','')
        ls = jieba.lcut(lines)
        for each in ls:
            if len(each) >= 2:
                d[each] = d.get(each,0) + 1
    ls1 = []
    lt = list(d.items())
    lt.sort(key = lambda x:x[1],reverse = True)
    for each in range(10):
        k,v = lt[each]
        ls1.append(k)
    return ls1
        
    
fi1 = "政府工作报告2019.txt"
fi2 = "政府工作报告2018.txt"


def compareWords(ls1, ls2):
    comm = []
    lt1 = []
    lt2 = []
    for i in ls1:
        if i in ls2:
            comm.append(i)
        else:
            lt1.append(i)
    for i in ls2:
        if i not in ls1:
            lt2.append(i)
    return comm, lt1, lt2
    
def show(common,y1,y2,l1,l2):
    print("共有词语:",end = '')
    print(",".join(common))
    print('{}特有:'.format(y1),end = '')
    print(','.join(l1))
    print("{}特有:".format(y2),end = '')
    print(','.join(l2))

def main():
    ls2019 = getwords(fi1)
    ls2018 = getwords(fi2)
    com,lst2019,lst2018 = compareWords(ls2019,ls2018)
    show(com,2019,2018,lst2019,lst2018)

main()