Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = {'吕布','关羽'}
type(x)
<class 'set'>
y = {'吕布':'口口布':'关羽':'关习习'}
SyntaxError: invalid syntax
y = {'吕布':'口口布':'关羽':'关习习'}
SyntaxError: invalid syntax
y = {'吕布':'口口布','关羽':'关习习'}
type(y)
<class 'dict'>
y['吕布']
'口口布'
y['刘备'] = '刘宝贝'
y['刘备']
'刘宝贝'
y
{'吕布': '口口布', '关羽': '关习习', '刘备': '刘宝贝'}
创建字典的方法：
SyntaxError: invalid character '：' (U+FF1A)
直接用大括号创建
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    直接用大括号创建
NameError: name '直接用大括号创建' is not defined
用dict函数进行创建
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    用dict函数进行创建
NameError: name '用dict函数进行创建' is not defined
b = dict(吕布 = '口口布',关羽 = '关习习',刘备 = '刘宝贝')
b
{'吕布': '口口布', '关羽': '关习习', '刘备': '刘宝贝'}
c = dict([('吕布',口口布'),('关羽','关习习'),('刘备','刘宝贝')])
           
SyntaxError: unterminated string literal (detected at line 1)
c = dict([('吕布',口口布'),('关羽','关习习'),('刘备','刘宝贝')])
           
SyntaxError: unterminated string literal (detected at line 1)
c = dict([('吕布','口口布'),('关羽','关习习'),('刘备','刘宝贝')])
           
c
           
{'吕布': '口口布', '关羽': '关习习', '刘备': '刘宝贝'}
f = dict(zip(['吕布','关羽','刘备'],['口口布','关习习
                               
SyntaxError: unterminated string literal (detected at line 1)
f = dict(zip(['吕布','关羽','刘备'],['口口布','关习习','刘宝贝']

             f
             
SyntaxError: '(' was never closed
f = dict(zip(['吕布','关羽','刘备'],['口口布','关习习','刘宝贝']))
             
f
             
{'吕布': '口口布', '关羽': '关习习', '刘备': '刘宝贝'}
d = dict.fromkeys('fish',250)
             
d
             
{'f': 250, 'i': 250, 's': 250, 'h': 250}
d['F'] = 70
             
d
             
{'f': 250, 'i': 250, 's': 250, 'h': 250, 'F': 70}
d.pop('s')
             
250
d.pop('狗')
             
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d.pop('狗')
KeyError: '狗'
d.pop('狗','没有')
             
'没有'
d.popitem()
             
('F', 70)
del d['i']
             
d
             
{'f': 250, 'h': 250}
del d
             
d
             
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
d = dict,fromkeys('FishC',250)
             
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    d = dict,fromkeys('FishC',250)
NameError: name 'fromkeys' is not defined
d = dict,fromkeys('FishC',250)
             
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    d = dict,fromkeys('FishC',250)
NameError: name 'fromkeys' is not defined
增：d[] 删d.pop减：del 除d.clear
             
SyntaxError: invalid character '：' (U+FF1A)






d = dict.fromkeys('FishC')
             
d
             
{'F': None, 'i': None, 's': None, 'h': None, 'C': None}
d['s'] = 115
             

d
             
{'F': None, 'i': None, 's': 115, 'h': None, 'C': None}
d.update({'i':105,'h':104})
             
d
             
{'F': None, 'i': 105, 's': 115, 'h': 104, 'C': None}
update传入多个键值对
             
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    update传入多个键值对
NameError: name 'update传入多个键值对' is not defined
d['C']
             
d['c']
             
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    d['c']
KeyError: 'c'
d.get('C','没有C')
             
\

d.get('c','没有C')
             
'没有C'
get查找键值，
             
SyntaxError: invalid character '，' (U+FF0C)
d.setdefault('C','code')
             
d.setdefault('c','code')
             
'code'
d
             
{'F': None, 'i': 105, 's': 115, 'h': 104, 'C': None, 'c': 'code'}
keys = d.keys()
             
values = d.values()
             
items = d.items()
             
items
             
dict_items([('F', None), ('i', 105), ('s', 115), ('h', 104), ('C', None), ('c', 'code')])
keys
             
dict_keys(['F', 'i', 's', 'h', 'C', 'c'])
values
             
dict_values([None, 105, 115, 104, None, 'code'])
items 键值对，keys键 values键值
             
SyntaxError: invalid character '，' (U+FF0C)
d.pop('C')
             
items
             
dict_items([('F', None), ('i', 105), ('s', 115), ('h', 104), ('c', 'code')])
e = d,copy
             
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    e = d,copy
NameError: name 'copy' is not defined
e = d,copy()
             
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    e = d,copy()
NameError: name 'copy' is not defined
\
e
             
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    e
NameError: name 'e' is not defined
e = d.copy
             
e
             
<built-in method copy of dict object at 0x000002B9C194BD40>
type(e)
             
<class 'builtin_function_or_method'>
list(d)
             
['F', 'i', 's', 'h', 'c']
list(d.values())
             
[None, 105, 115, 104, 'code']
e = iter(d)
             
e
             
<dict_keyiterator object at 0x000002B9C37A81D0>
next(e)
             
'F'
next(e)
             
'i'
next(e)
             
's'
next(e)
             
'h'
next(e)
             
'c'
next(e)
             
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    next(e)
StopIteration
iter 创建迭代器
             
SyntaxError: invalid syntax
reversed(d)
             
<dict_reversekeyiterator object at 0x000002B9C193D260>
d
             
{'F': None, 'i': 105, 's': 115, 'h': 104, 'c': 'code'}
d.reversed()
             
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    d.reversed()
AttributeError: 'dict' object has no attribute 'reversed'
list(reversed(d.values))
             
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    list(reversed(d.values))
TypeError: 'builtin_function_or_method' object is not reversible
list(reversed(d.values()))
             
['code', 104, 115, 105, None]
d = {'吕布':{'语文':60,'数学':70,'英语':80},'关羽':{'语文':80,'数学':90,'英语':70}}
             
d
             
{'吕布': {'语文': 60, '数学': 70, '英语': 80}, '关羽': {'语文': 80, '数学': 90, '英语': 70}}
d['吕布']['数学']
             
70
d = {'F':70,'i':105,'s':115,'h':104,'c':67}
             
b = {v:k for k,v in d.items()}
             
b
             
{70: 'F', 105: 'i', 115: 's', 104: 'h', 67: 'c'}
d
             
{'F': 70, 'i': 105, 's': 115, 'h': 104, 'c': 67}
