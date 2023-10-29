from concurrent.futures import ThreadPoolExecutor
import time
from functools import partial
from threading import Thread


def out1():
    while True:
        print('ping', end='', flush=True)
        time.sleep(0.001)


def out2():
    while True:
        print('pong', end='', flush=True)
        time.sleep(0.001)


def main():
    Thread(target=out1).start()
    Thread(target=out2).start()
    with ThreadPoolExecutor(max_workers=10) as pool:  # 线程创建
        f = pool.submit(out1, args=)


main()


"""
def out(content):
    while True:
    print(content,end = '',flush = True)
    time.sleep(0.001)
    

out1 = partial(out,content = 'ping')
out2 = partial(out,content = 'pong')    

def main():
    Thread(target= out ,args = ('ping, )元组参数).start().join()
    Thread(target= out ,args = ('pong, )元组参数).start().join()

# join()表示等待进程结束


main()
"""
