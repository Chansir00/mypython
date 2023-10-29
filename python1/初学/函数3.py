Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('小甲鱼')
小甲鱼
print('小甲鱼','爱','Python')
小甲鱼 爱 Python
def myfunc(*args):
    print('有{}个参数。'.format(len(args)))
    print('第二个参数是{}'.format(args[1]))

    
myfunc('小甲鱼','不二')
有2个参数。
第二个参数是不二
def myfun():
    return 1,2,3
myfunc()
SyntaxError: invalid syntax
def myfun():
    return 1,2,3
myfun()
SyntaxError: invalid syntax
mufunc(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    mufunc(1,2,3,4,5)
NameError: name 'mufunc' is not defined. Did you mean: 'myfunc'?
def myfunc():
    return1,2,3

    
myfunc()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    myfunc()
  File "<pyshell#14>", line 2, in myfunc
    return1,2,3
NameError: name 'return1' is not defined
myfunc()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    myfunc()
  File "<pyshell#14>", line 2, in myfunc
    return1,2,3
NameError: name 'return1' is not defined
myfunc(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    myfunc(1,2,3,4,5)
TypeError: myfunc() takes 0 positional arguments but 5 were given
def myfunc(*args):
    print(args)

    
myfunc(1,2,3,4,5)
(1, 2, 3, 4, 5)
myfunc(1,2,3,a=4,b=5)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    myfunc(1,2,3,a=4,b=5)
TypeError: myfunc() got an unexpected keyword argument 'a'
def myfunc(**kwargs):
    print(kwargs)

    
myfunc(a=1,b=2,c=3)
{'a': 1, 'b': 2, 'c': 3}
def myfunc(a,*b,**c):
    print(a,b,c)

    
myfunc(1,2,3,4,x=5,y=6)
1 (2, 3, 4) {'x': 5, 'y': 6}
help(str.format)
Help on method_descriptor:

format(...)
    S.format(*args, **kwargs) -> str
    
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').

args = (1,2,3,4)
def myfunc(a,b,c,d):
    print(a,b,c,d)

    
myfunc(args)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    myfunc(args)
TypeError: myfunc() missing 3 required positional arguments: 'b', 'c', and 'd'
myfunc(*args)
1 2 3 4
kwargs = {'a':1,'b':2,'c':3,'d':4}
myfunc(**kwargs)
1 2 3 4
