import random 
def main():
    proA,proB,n = getinputs()
    printintro(n)
    winA,winB = getWingames(n,proA,proB)
    printconclude(winA,winB)

def printintro(n):
    print("本次比赛将根据球员能力值进行{}次比赛".format(n))

def getinputs():
    proA = eval(input("请输入A球员的能力值"))
    proB = eval(input("请输入B球员的能力值"))
    n = eval(input("请输入比赛场次"))
    return proA,proB,n

def getWingames(n,proA,proB):
    print("比赛开始")
    winA ,winB = 0,0
    for i in range(n):
        temp = getonegame(proA,proB)
        if temp == 'Awin':
            winA +=1
        else:
            winB += 1
    return winA,winB

def getonegame(proA,proB):
    scoreA ,scoreB = 0,0
    start = 'A'
    if start == 'A':
        if random.random() < proA:
            scoreA += 1
        else:
            start = 'B'
    else:
        if random.random() < proB:
            scoreB += 1
        else:
            start = 'A'
    if scoreA == 15:
        return 'Awin' 
    elif scoreB == 15:
        return 'Bwin'
    
def printconclude(winA,winB):
    n = winA + winB
    print("共模拟了{}场比赛".format(n))
    print('选手A获胜{}场比赛，占比{}'.format(winA,winA/n))
    print('选手B获胜{}场比赛，占比{}'.format(winB,winB/n))

main()