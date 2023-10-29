Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#类：模具
#继承：子类。父类
class A:
    x = 520
    def hello(self):
        print('你好')

        
class B(A):
    pass

b = B()
b.x
520
b/hello
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b/hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
b.hello
<bound method A.hello of <__main__.B object at 0x00000173BCA10760>>
b.hello()
你好
class B(A):
    x = 880
    def hello(self):
        print('你好')

        
b = B()
b.x
880
b.hello()
你好
isinstance(b,B)
True
issubclass(A,B)
False
issubclass(B,A)
True
#多重继承
class B:
    x = 880
    y = 250
    def hello(self)
    
SyntaxError: expected ':'
class B:
    x = 880
    y = 250
    def hello(self)：
    
SyntaxError: invalid character '：' (U+FF1A)
class B:
    x = 880
    y = 250
    def hello(self):
        print('hello')

        
class C(A,B):
    pass

c = C()
c.x
520
c.heelo
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    c.heelo
AttributeError: 'C' object has no attribute 'heelo'. Did you mean: 'hello'?
c.hello
<bound method A.hello of <__main__.C object at 0x00000173BCA11DB0>>
c.hello()
你好
c.y
250
#组合
class Turtle:
    def say(self):
        print('hello')

        
class cat:
    def say(self):
        print('喵喵')

        
class dog:
    def sat(self):
        print('我是小狗')

        
class Garden:
    t = Turtle()
    c = cat
    d = dog
    def say(self):
        self.t.say()
        self.c.say()
        selg.d.say()

        
g = Garden()
g.say()
hello
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    g.say()
  File "<pyshell#65>", line 7, in say
    self.c.say()
TypeError: cat.say() missing 1 required positional argument: 'self'
class Garden:
    t = Turtle()
    c = cat
    d = dog
    def say(self):
        self.t.say()
        self.c.say()
        self.d.say()

        
g.say()
hello
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    g.say()
  File "<pyshell#65>", line 7, in say
    self.c.say()
TypeError: cat.say() missing 1 required positional argument: 'self'
#类和对象
