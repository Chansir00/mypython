Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def add(x,y):
    return x +y

import functools
functools.reduce()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    functools.reduce()
TypeError: reduce expected at least 2 arguments, got 0
functools.reduce(add,[1,2,3,4,5])
15
add(add(add(add(1,2),3),4),5)
15
functools.reduce(lambda x,y:x*y,range(1,10))
362880
square = functools.partial(pow,exp=2)
squre(2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    squre(2)
NameError: name 'squre' is not defined. Did you mean: 'square'?
square(2)
4
cube = functools.partial(pow,exp=3)
cube(3)
27
myfunx.name
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    myfunx.name
NameError: name 'myfunx' is not defined
myfunx._name_
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    myfunx._name_
NameError: name 'myfunx' is not defined
open('FishC.txt')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    open('FishC.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'FishC.txt'
open('FishC.txt','w')
<_io.TextIOWrapper name='FishC.txt' mode='w' encoding='cp936'>
f.write('I love Python')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    f.write('I love Python')
NameError: name 'f' is not defined
f = open('Fishc.txt','w')
f.write('I love Python')
13
f.writelines(['I love FishC.\n','I love Python'])
f = open('Fishc.txt','r+')
f.redable()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    f.redable()
AttributeError: '_io.TextIOWrapper' object has no attribute 'redable'. Did you mean: 'readable'?
f.readable()
True
f.writable()
True
for each in f:
    print(each)

    
I love PythonI love FishC.

I love Python
f.read()
''
f.tell()
41
f.seek(0)
0
f.read()
'I love PythonI love FishC.\nI love Python'
f.write('I love my wife')
14
f.flush()
f
<_io.TextIOWrapper name='Fishc.txt' mode='r+' encoding='cp936'>
f.truncate(29)
29
f.close()
f.open('FishC.txt,'w')
       
SyntaxError: unterminated string literal (detected at line 1)
f.open('FishC.txt','w')
       
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    f.open('FishC.txt','w')
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
f = open('FishC.txt','w')
       
f.close()
       
 