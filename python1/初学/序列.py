Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = [1,2,3,0,6]
sorted(S)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    sorted(S)
NameError: name 'S' is not defined. Did you mean: 's'?
sorted(s)
[0, 1, 2, 3, 6]
sort函数排大小
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    sort函数排大小
NameError: name 'sort函数排大小' is not defined
key(s)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    key(s)
NameError: name 'key' is not defined
sorted(s,reverse=True)
[6, 3, 2, 1, 0]
reverse反转
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    reverse反转
NameError: name 'reverse反转' is not defined
t = ['fichc','apple','book','pen']
\
sorted(t)
['apple', 'book', 'fichc', 'pen']
sorted(t,key=len)
['pen', 'book', 'fichc', 'apple']
排序方法：比较第一个字符顺序，其中大写字母小于小写字母，第一个字母相同则比较第二个字母
SyntaxError: invalid character '：' (U+FF1A)
sorted('fishc')
['c', 'f', 'h', 'i', 's']
s = [1,2,5,8,0]
reverse(s)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    reverse(s)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
reversed(s)
<list_reverseiterator object at 0x00000208B87D3340>
list(reversed(s))
[0, 8, 5, 2, 1]
s.reverse()
s
[0, 8, 5, 2, 1]
[0, 8, 5, 2, 1]
[0, 8, 5, 2, 1]




x = [1,1,0]
y = [1,1,9]
all(x)
False
all(y)
True
any(x)
True
any(y)
True
seasons = ['spring','summer','fall','winter']
enumerrate(season)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    enumerrate(season)
NameError: name 'enumerrate' is not defined. Did you mean: 'enumerate'?
enumerrate(seasons)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    enumerrate(seasons)
NameError: name 'enumerrate' is not defined. Did you mean: 'enumerate'?
enumerate(seasons)
<enumerate object at 0x00000208B87DDD40>
list(enumerate(seasons))
[(0, 'spring'), (1, 'summer'), (2, 'fall'), (3, 'winter')]
x = [1,2,3]
y = [4,5,6]
zip(x,y)
<zip object at 0x00000208B86D6140>
list(zipped)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list(zipped)
NameError: name 'zipped' is not defined
list(zip)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    list(zip)
TypeError: 'type' object is not iterable
zipped = zip(x,y)

list(zipped)
[(1, 4), (2, 5), (3, 6)]
z = 'fishc'
zipped = zip(x,y,z)
list(zipped)
[(1, 4, 'f'), (2, 5, 'i'), (3, 6, 's')]
import itertools
itertools.zip_longist(x,y,z)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    itertools.zip_longist(x,y,z)
AttributeError: module 'itertools' has no attribute 'zip_longist'. Did you mean: 'zip_longest'?
zipped = itertools.zip_longist(x,y,z)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    zipped = itertools.zip_longist(x,y,z)
AttributeError: module 'itertools' has no attribute 'zip_longist'. Did you mean: 'zip_longest'?
zipped = itertools.zip_longest(x,y,z)
list(zipped)
[(1, 4, 'f'), (2, 5, 'i'), (3, 6, 's'), (None, None, 'h'), (None, None, 'c')]
引入itertools工具，是所有可迭代量全部打印
SyntaxError: invalid character '，' (U+FF0C)
mapped = map(ord,'fishc')
list(mapped)
[102, 105, 115, 104, 99]
map(pow,[2,3,10],[5,2,3])
<map object at 0x00000208B87D3A90>
list(map)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    list(map)
TypeError: 'type' object is not iterable
mapped = map(pow,[2,3,10],[5,2,3])
list(mapped)
[32, 9, 1000]
pow函数计算x的y次幂
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    pow函数计算x的y次幂
NameError: name 'pow函数计算x的y次幂' is not defined
list(filter(str.islower,'Fishc'))
['i', 's', 'h', 'c']
\
filter过滤器
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    filter过滤器
NameError: name 'filter过滤器' is not defined
mapped = map(ord,'Fishc')
for each in mapped:
    print(each)

    
70
105
115
104
99
list(mapped)
[]
x = [1,2,3,4,5]
y = iter(x)
iter函数设置迭代器
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    iter函数设置迭代器
NameError: name 'iter函数设置迭代器' is not defined
type(x)
<class 'list'>
type(y)
<class 'list_iterator'>
next(y)
1
next(y)
2
next(y)
3
next(y)
4
next(y)
5
next(y)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    next(y)
StopIteration
