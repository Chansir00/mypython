from concurrent.futures import ThreadPoolExecutor
import time
from threading import Thread,RLock,current_thread,Condition
import random
'''
多个线程竞争一个资源 --> 临界资源
保护临界资源：在一个时刻只能有一个人操作：给资源加锁 
'''

class Account:

    def __init__(self):
        self.balance=0 
        #self.lock = RLock()
        self.condition = Condition(RLock())

    #存钱    
    def deposite(self,money):
        #self.lock.acuqire()
        with self.condition:     #上下文管理器
            new_balance = self.balance + money
            time.sleep(0.01)
            self.balance = new_balance
            #唤醒线程让他们恢复运行
            self.condition.notify_all()
        #self.lock.realease
    #取钱
    def withdraw(self,money):
        with self.condition:
        #检查金额是否足够
            while self.balance < money:
                self.condition.wait() 
            new_balance = self.balance - money
            time.sleep(0.01)
            self.balance = new_balance
        

def put_money(account):
    while True:
        money = random.randint(5,10)
        account.deposite(money)
        current = current_thread()
        print("{}存入{}元，当前余额{}".format(current.name,money,account.balance))
        time.sleep(1)

def get_money(account):
    while True:
        money = random.randint(10,20)
        account.withdraw(money)
        current = current_thread()
        print("{}取出{}元，当前余额{}".format(current.name,money,account.balance))
        time.sleep(0.5)

    
def main():
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for i in range(5):
            pool.submit(put_money,account)
            pool.submit(get_money,account)

    print(account.balance)

if __name__ == '__main__':
    main()


