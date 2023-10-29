Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
[1,2,3,4,5]
[1, 2, 3, 4, 5]
[1,2,3,"上山打老鼠"]
[1, 2, 3, '上山打老鼠']
rhyme = [1,2,3,4,5,'上山打老虎']
print(rhume)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(rhume)
NameError: name 'rhume' is not defined. Did you mean: 'rhyme'?
print(rhyme)
[1, 2, 3, 4, 5, '上山打老虎']
for each in rhyme:
    print(each)

1
2
3
4
5
上山打老虎
rhyme[0]
1
rhyme[5]
'上山打老虎'
a = [1,2,3,4]
a[3]
4
len(rhyme)
6
length  = len(rhyme)

rhyme[-1]
'上山打老虎'
rhyme[0:3]
[1, 2, 3]
rhyme[3:6]
[4, 5, '上山打老虎']
rhyme [:3]
[1, 2, 3]
rhyme[:]
[1, 2, 3, 4, 5, '上山打老虎']
rhyme[:4]
[1, 2, 3, 4]
range(3,5)
range(3, 5)
range(1,100,2)
range(1, 100, 2)
rhyme[::1]
[1, 2, 3, 4, 5, '上山打老虎']
rhyme[::2]
[1, 3, 5]
heros = ['钢铁侠','路巨人']
heros.append('黑寡妇')
heros
['钢铁侠', '路巨人', '黑寡妇']
heros.expend(['鹰眼''灭吧''；欸神'])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    heros.expend(['鹰眼''灭吧''；欸神'])
AttributeError: 'list' object has no attribute 'expend'. Did you mean: 'extend'?
heros.expend(['鹰眼''灭吧''欸神'])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    heros.expend(['鹰眼''灭吧''欸神'])
AttributeError: 'list' object has no attribute 'expend'. Did you mean: 'extend'?
heros.expend(['鹰眼','灭吧','欸神'])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    heros.expend(['鹰眼','灭吧','欸神'])
AttributeError: 'list' object has no attribute 'expend'. Did you mean: 'extend'?
heros.extend(['鹰眼','灭吧','欸神'])
heros
['钢铁侠', '路巨人', '黑寡妇', '鹰眼', '灭吧', '欸神']
s = [1,2,3,4,5]
s[len (s):] = [6]
s
[1, 2, 3, 4, 5, 6]
s[len(s):] = [7,8,9]
s
[1, 2, 3, 4, 5, 6, 7, 8, 9]
s[len(s):] = [2]
s
[1, 2, 3, 4, 5, 6, 7, 8, 9, 2]
s[len (s):] = ['花时间']
s
[1, 2, 3, 4, 5, 6, 7, 8, 9, 2, '花时间']
s.insert(1,2)
s
[1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 2, '花时间']
heros.remove('灭吧')
heros
['钢铁侠', '路巨人', '黑寡妇', '鹰眼', '欸神']
heros.pop(2)
'黑寡妇'
heros.pop(2)
'鹰眼'
heros
['钢铁侠', '路巨人', '欸神']
