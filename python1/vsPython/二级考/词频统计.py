import jieba
dk = {}

with open('data.txt','r',encoding= 'utf-8') as f:
    sl = f.readlines()
for s in sl:
    k = jieba.lcut(s,cut_all = True)
    for wo in k:
        if len(wo) == 2:
            dk[wo] = dk.get(wo,0) + 1

dp = list(dk.items())
dp.sort(key = lambda x :int(x[1]),reverse= True)

for i in range(10):
    print("{}:{}".format(dp[i][0],dp[i][1]))