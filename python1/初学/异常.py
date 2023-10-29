Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1 / 10
0.1
thy:
    
SyntaxError: invalid syntax
try:
    1 / 0
except:
    peint('出错了')

    
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    1 / 0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#6>", line 4, in <module>
    peint('出错了')
NameError: name 'peint' is not defined. Did you mean: 'print'?
try:
    1 / 0
except:
    print('出错了')

    
出错了
##检测异常
try:
    520 + 'FishC'
except ZeroDivisionError
SyntaxError: expected ':'
try:
    520 + 'FishC'
except ZeroDivisionError:
    print('出错了')

    
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    520 + 'FishC'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
##指定检测错误
try:
    1 / 0
    520 + 'FISHC'
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('值不正确')
except TypeError:
    print("类型不正确")

    
除数不能为0
#捕获到异常直接结束