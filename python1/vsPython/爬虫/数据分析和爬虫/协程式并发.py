import asyncio

#normal abnormal
#symmetric asymmetric
# synchronous asynchronous
# 被async修饰的函数是异步函数，调用异步函数不是直接获取返回值
#而是创造一个协程对象，可以和其他子程序相互协作的程序

async def display(num):
    print(num)
    await asyncio.sleep(1)


cost_list = [display(n) for n in range(1,11)]

#启动一个事件循环，将协程对象注册到事件循环内（注册后才能协作）
loop = asyncio.get_event_loop()
#将列表中的对象处理成一个Task对象然后挂到事件循环上
#相当于将十个协程对象都注册到事件循环。
loop.run_until_complete(asyncio.wait(cost_list))