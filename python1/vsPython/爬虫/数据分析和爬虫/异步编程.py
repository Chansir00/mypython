'''
迭代器：实现迭代器协议的方法
__iter__
__next__
'''

class rabit:

    def __init__(self,num):
        self.a,self.b = 0,1
        self.count = 0
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num:
            self.a = self.b
            self.b = self.a + self.b
            self.count += 1
            return self.a
        raise StopIteration


rabit1 = rabit(2)
for value in rabit1:
    print(value)
    

'''
生成器：迭代器语法简化版
生成器表达式：(num for num in range(100))
'''

def fib(num):
    a,b = 0,1
    for _ in range(num):
        a,b = b,a+b
        yield a

#调用函数不是简单的返回值，而是生成了一个生成器对象
fiber = fib(1)
print(type(fiber))
for value in fiber:
    print(value)


items = [22,33,44,55,66]
iter = iter(items)
print(type(iter))
print(next(iter))


'''创建生成器的两种方法
def create_num_gen():
    for num in range(1,100,2):
        yield num

num = (num for num in range(1,100,2)))
'''


'''
协程
'''

def count_avg_value():
    total,count,avg = 0,0,None
    while True:
        current_value = yield
        total += current_value
        count += 1
        avg = total/count
        print(f'平均值是{avg}')

def main():
    gen = count_avg_value()
    #对生成器进行预激活，使生成器变成协程对象
    gen.send(None)
    gen.send(10)
    gen.send(20)
    gen.send(30)

if __name__ == '__main__':
    main()