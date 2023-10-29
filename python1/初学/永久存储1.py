Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
openn('FishC.txt','w')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    openn('FishC.txt','w')
NameError: name 'openn' is not defined. Did you mean: 'open'?
open('FishC.txt','w')
<_io.TextIOWrapper name='FishC.txt' mode='w' encoding='cp936'>
f = open('FishC.txt','w')
f.write('I love FishC')
12
f.close()
#打开文件，操作文件，关闭文件
with open('FishC.txt','w') as f:
    f.write("I love FishC")

    
12
#不用关闭文件
#不用关闭文件
#pickle 永久存储Pyhon对象
x,y,z=1,2,3

============= RESTART: C:/Users/64271/AppData/Local/Programs/Python/Python310/永久存储.py ============
Traceback (most recent call last):
  File "C:/Users/64271/AppData/Local/Programs/Python/Python310/永久存储.py", line 9, in <module>
    pickle.dunp(y,f)
AttributeError: module 'pickle' has no attribute 'dunp'. Did you mean: 'dump'?

============= RESTART: C:/Users/64271/AppData/Local/Programs/Python/Python310/永久存储.py ============
