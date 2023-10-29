Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 '     左侧不要留白'.lstrip()
 
SyntaxError: unexpected indent
'     左侧不要留白'.lstrip()
'左侧不要留白'
'       右侧不要留白'.rstrip()
'       右侧不要留白'
'   左右都不要留白    '.strip()
'左右都不要留白'
'www.ilovefishc.com'removeprefix('www.')
SyntaxError: invalid syntax
'www.ilovefishc.com'removeprefix('www.')
SyntaxError: invalid syntax
'www.ilovefishc.com'.removeprefix('www.')
'ilovefishc.com'
'www.ilovefishc.com'.patition('.')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    'www.ilovefishc.com'.patition('.')
AttributeError: 'str' object has no attribute 'patition'. Did you mean: 'partition'?

'www.ilovefishc.com'.patition('.')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    'www.ilovefishc.com'.patition('.')
AttributeError: 'str' object has no attribute 'patition'. Did you mean: 'partition'?
".".join(["www"，"ilovefishc"，"com"])
SyntaxError: invalid character '，' (U+FF0C)
".".join(["www","ilovefishc","com"])
'www.ilovefishc.com'
"^".join(("F","ish","c"))
'F^ish^c'
s = "fishc"
s
'fishc'
s += s
s
'fishcfishc'
"".join(("fishc","fishc"))
'fishcfishc'





year = 2010
"鱼C工作室成立于 year 年“
SyntaxError: unterminated string literal (detected at line 1)
"鱼C工作室成立于 year 年"
'鱼C工作室成立于 year 年'
"鱼C工作室成立于 {} 年".format(year)
'鱼C工作室成立于 2010 年'
"(1)看到{0}就很激动！".format("小甲鱼","漂亮的小姐姐")
'(1)看到小甲鱼就很激动！'
"{1}看到{0}就很激动！".format("小甲鱼","漂亮的小姐姐")
'漂亮的小姐姐看到小甲鱼就很激动！'
"{0}{0}{1}{1}".format("是","非")
'是是非非'
"我叫{name}.我爱{fav}".format(name = '小甲鱼', fav = 'Pyho')
'我叫小甲鱼.我爱Pyho'
'{:^}',format()250
SyntaxError: invalid syntax
'{:^}',format(250)
('{:^}', '250')
"{:^}",format(250)
('{:^}', '250')
"{:^}".format(250)
'250'
'{:^10}'.format(250)
'   250    '
'{1:>10}{0:<10}'.format(right=520,left=250)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    '{1:>10}{0:<10}'.format(right=520,left=250)
IndexError: Replacement index 1 out of range for positional args tuple
'{1:>10}{0:<10}'.format(520,250)
'       250520       '
'{left:>10}{right:<10}'.format(right=520,left=250)
'       250520       '
'{:010}'.format(520)
'0000000520'
