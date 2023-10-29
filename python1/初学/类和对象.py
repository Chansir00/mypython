Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
try:
    1 / 0
except:
    print("逮到了")

    
逮到了
try:
    1 / 1
except:
    print('逮到了')
else:
    print('没逮到')

    
1.0
没逮到
try:
    1 / 0
except:
    print('没逮到')
else:
    print('逮到了')
finally:
    print('带没逮到都说一声')

    
没逮到
带没逮到都说一声
try:
    f = open('Fishc.txt','w')
    f.write('I love FishC')
except:
    print('出错了“）
          
SyntaxError: unterminated string literal (detected at line 5)
try:
    f = open('Fishc.txt','w')
    f.write('I love FishC')
except:
    print('出错了'）
          
SyntaxError: invalid character '）' (U+FF09)
try:
    f = open('Fishc.txt','w')
    f.write('I love FishC')
except:
    print('出错了')
finally:
    f.close()

    
12
try:
    while True:
        pass
finally:
    print('晚安')

    
晚安
Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    while True:
KeyboardInterrupt


try:
    try:
        520 + 'FichC'
    except:
        print('内部异常')
    1 / 0
except:
    print('外部异常')
finally:
    print('收尾工作')

    
内部异常
外部异常
收尾工作
raise FishCError('小甲鱼不行')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    raise FishCError('小甲鱼不行')
NameError: name 'FishCError' is not defined
try:
    1 / 0
except:
    raise ValueError('这样不行')

Traceback (most recent call last):
  File "<pyshell#53>", line 2, in <module>
    1 / 0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#53>", line 4, in <module>
    raise ValueError('这样不行')
ValueError: 这样不行
raise ValueError('这样可不行')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    raise ValueError('这样可不行')
ValueError: 这样可不行
raise ValueError('这样可不行') from ZeroDivisionError
ZeroDivisionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    raise ValueError('这样可不行') from ZeroDivisionError
ValueError: 这样可不行
s = 'FishC'
assert s == 'FishC'
assert s == 'Fishc'
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    assert s == 'Fishc'
AssertionError
##类和对象
##class 创建类
#self参数
class C:
    def hello():
        print('你好')

        
c = C()
c.hello()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    c.hello()
TypeError: C.hello() takes 0 positional arguments but 1 was given
class C:
    def get_self(self):
        print(self)

        
c = C()
c.get_self()
<__main__.C object at 0x000001AB8EAF1BD0>
c
<__main__.C object at 0x000001AB8EAF1BD0>
