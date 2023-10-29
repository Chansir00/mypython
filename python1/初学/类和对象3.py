Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Turtle:
    head = 1
    eyes = 2
    legs = 4
    shell = True

    
class Turtle:
    head = 1
    eyes = 2
    legs = 4
    shell = True
    def crawl(self)
    
SyntaxError: expected ':'
class Turtle:
    head = 1
    eyes = 2
    legs = 4
    shell = True
    def crawl(self):
        print('人们总抱怨我慢吞吞的，殊不知不积跬步无以至千里')
    def run(self):
        print('虽然我行动很慢，但如果遇到危险，还是会拼命狂奔的')
    def bite(self):
        print('人善被人欺，龟善被人骑')
    def eat(self):
        print('谁知盘中餐，粒粒皆辛苦')
    def sleep(self):
        print('Zzzzz..')

        
t1 = Turtle()
t1.legs
4
t1.crawl()
人们总抱怨我慢吞吞的，殊不知不积跬步无以至千里
t1.sleep()
Zzzzz..
t2 = Turtle
t2.legs()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    t2.legs()
TypeError: 'int' object is not callable
t2.legs
4
t2.legs = 3
t2.legs
3
#Turtle 为类，一般类名为大写开头，改变她
#Turtle 为类，一般类名为大写开头，改变t2不改变t1
t1.mouth = 1
dir(t1)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bite', 'crawl', 'eat', 'eyes', 'head', 'legs', 'mouth', 'run', 'shell', 'sleep']
#封装：将特征封装到一起
x = 520
type(x)
<class 'int'>
y = 'FISHC'
type(y)
<class 'str'>
#x,y均为实例对象
