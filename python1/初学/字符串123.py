Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 'I love Fishc'
x.capitalize()
'I love fishc'
x
'I love Fishc'
x.casefold()
'i love fishc'
x.title()
'I Love Fishc'
x.swapcase()
'i LOVE fISHC'
x.upper()
'I LOVE FISHC'
x.lower()
'i love fishc'
x = '有内鬼，停止交易'
x.center(2)
'有内鬼，停止交易'
x.center(15)
'    有内鬼，停止交易   '
x.ljust(15)
'有内鬼，停止交易       '
x.rjust(15)
'       有内鬼，停止交易'
x.zfill(15)
'0000000有内鬼，停止交易'
x.rjust(15.'淦')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
x
'有内鬼，停止交易'
x.rjust(15,'淦')
'淦淦淦淦淦淦淦有内鬼，停止交易'
x = jajijflkajiw
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x = jajijflkajiw
NameError: name 'jajijflkajiw' is not defined
x = fssf
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x = fssf
NameError: name 'fssf' is not defined
x
'有内鬼，停止交易'
a = dsfaf
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a = dsfaf
NameError: name 'dsfaf' is not defined
x = '上海自来水来自海上'
x.count('海'，0，5)
SyntaxError: invalid character '，' (U+FF0C)
x.count('海',0,5)
1
x.find('龟')
-1
code =
SyntaxError: invalid syntax
code
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    code
NameError: name 'code' is not defined
code = '''
    print('i love fish')
print('i lobe fish')'''


new_code = code.expandtabs(4)
print(new_code)

    print('i love fish')
print('i lobe fish')
'在吗，我在你家楼下！！！‘
SyntaxError: unterminated string literal (detected at line 1)
'在吗，我在你家楼下！！！'
'在吗，我在你家楼下！！！'
'在吗，我在你家楼下！！！'.replace('在吗，想你')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    '在吗，我在你家楼下！！！'.replace('在吗，想你')
TypeError: replace expected at least 2 arguments, got 1
'在吗，我在你家楼下！！！'.replace('在吗'，'想你')
SyntaxError: invalid character '，' (U+FF0C)
'在吗，我在你家楼下！！！'.replace('在吗','想你')
'想你，我在你家楼下！！！'
str.maketrans('ABCDEFG','1234567')
{65: 49, 66: 50, 67: 51, 68: 52, 69: 53, 70: 54, 71: 55}
table = str.maketrans('ABCDEFG','1234567')
'I love FishC'.translate(table)
'I love 6ish3'
'I love FishC'.translate(str.maketrans('ABCDEFG','1234567','love'))
'I  6ish3'
x = '我爱Python'
x.startswith('我")
             
SyntaxError: unterminated string literal (detected at line 1)
x.startswith('我’)
             
SyntaxError: unterminated string literal (detected at line 1)
x.startswith('我')
             
True
x.stratswith('你')
             
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x.stratswith('你')
AttributeError: 'str' object has no attribute 'stratswith'. Did you mean: 'startswith'?
x.startswith('你')
             
False
x.startswith('我',1)
             
False
x = '她爱Pyrhon'
             
if x.startswith(('你','我','他'))
             
SyntaxError: expected ':'
if x.startswith(('你','我','他')):
             print('总有人喜欢Pyhon')

             
x
             
'她爱Pyrhon'
x = 'I love Python'
             
x.isalpha()
             
False
'IlovePython'.isalpha()
             
True
'    \n'.isspace()
             
True
x = '2²'
             
x.isdecimal()
             
False
x.isdigit()
             
True
x.isnumeric()
             
True\
x =
             
SyntaxError: invalid syntax
x = 'ⅠⅡⅢ'
             
x.isdecimal()
             
False
x.isdigit()
             
False
x.isnumeric()
             
True
x = '一二三四五'
             
x.ismumeric()
             
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    x.ismumeric()
AttributeError: 'str' object has no attribute 'ismumeric'. Did you mean: 'isnumeric'?
x.isnumeric()
             
True
