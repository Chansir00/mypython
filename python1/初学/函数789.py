Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
map(lambda x :ord(x) + 10,'FichC')
<map object at 0x000001737BAB0760>
mapped = map(lambda x :ord(x) + 10,'FichC')
list(mapped)
[80, 115, 109, 114, 77]
list(filter(lambda x :x % 2,range(10)))
[1, 3, 5, 7, 9]
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1

        
counter()
<generator object counter at 0x000001737BA6B450>
for i in counter():
    print(i)

    
0
1
2
3
4
5
c = counter()
c
<generator object counter at 0x0000017379995F50>
next(c)
0
next(c)
1
next(c)
2
next(c)
3
next(c)
4
next(c)
5
next(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    next(c)
StopIteration
def fib():
    i = 0
    n = 1
    while True:
        yield i
        i,n = n, i + n

        
f = fib()
next(f)
0
next(f)
1
next(f)
1
next(f)
2
next(f)
3
next(f)
5
next(f)
8
next(f)
13
next(f)
21
next(f)
34
next(f)
55
next(f)
89
next(f)
144
next(f)
233
def funA():
    print('AWBDYL')

    
def funB():
    funA()

    
def funC():
    print('AWDBYL')
    func

    
def funC():
    print('AWDBYL')
    funC

    
funC
<function funC at 0x000001737BAE4CA0>
funC()
AWDBYL
def funC():
    print('AWDBYL')
    funC()

    
funC()
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
AWDBYL
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    funC()
  File "<pyshell#60>", line 3, in funC
    funC()
  File "<pyshell#60>", line 3, in funC
    funC()
  File "<pyshell#60>", line 3, in funC
    funC()
  [Previous line repeated 146 more times]
  File "<pyshell#60>", line 2, in funC
    print('AWDBYL')
KeyboardInterrupt
def funC(i):
    if i > 0:
        print('AWBDYL')
        i -= 1
        funC(i)

        
funC(10)
AWBDYL
AWBDYL
AWBDYL
AWBDYL
AWBDYL
AWBDYL
AWBDYL
AWBDYL
AWBDYL
AWBDYL
def myfunc(n):
    result = n
    for i in range(1,n)
    
SyntaxError: expected ':'
def myfunc(n):
    result = n
    for i in range(1,n):
        result *= 1
    return result

myfunc(4)
4

myfunc(5）
       
SyntaxError: invalid decimal literal
myfunc(5)
       
5
def myfunc(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
myfun(5)
SyntaxError: invalid syntax
def myfunc(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
myfun(5)
SyntaxError: invalid syntax
myfunc(5)
5
def myfunc(n):
    result = n
    for i in range(1,n)
    
SyntaxError: expected ':'
def myfunc(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

myfunc(5)
120
def myfunA(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c
myfunA(12)
SyntaxError: invalid syntax
def myfunA(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c
myfunA(12)
SyntaxError: invalid syntax

def myfunA(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c


myfunA(12)
144
def myfunB(n)
SyntaxError: expected ':'
def myfunB(n):
    if n == 1 or n == 2
    
SyntaxError: expected ':'
def myfunB(n):
    if n == 1 or n == 2:
        return 1
    else:
        return myfunB(n-1) + myfunB(n-2)

    
\myfunB(12)
144
myfunA(120)
5358359254990966640871840
