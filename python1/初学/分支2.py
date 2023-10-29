Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ma = [[1,2,3],[4,5,6],[7,8,9]]
ma
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
SyntaxError: invalid syntax
ma
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ma = [[1,2,3]]
ma = [[1,2,3],
      [4,5,6],
      [7,8,9]]
ma
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in ma
SyntaxError: expected ':'
ma
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in ma:
    for each in (i):
        print(each)

        
1
2
3
4
5
6
7
8
9
for each in ma:
    print(each)

    
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
for i in ma:
    for each in i:
        print(each,end=' ')
        print()

        
1 
2 
3 
4 
5 
6 
7 
8 
9 
for i in ma:
    for each in (i):
        print(each,end=' ')
    print()

    
1 2 3 
4 5 6 
7 8 9 
ma[0]
[1, 2, 3]
ma[0][0]
1
ma[2][2]
9
a = 0*3
a = [0] *3
a
[0, 0, 0]
for i in range(3):
    a[i] = [0] * 3
    a

    
[[0, 0, 0], 0, 0]
[[0, 0, 0], [0, 0, 0], 0]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = [0*3]*3
b
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]

b = [[0]*3]*3
b
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a is b
False
0 is 0
True
x = [1,2,3]
y = [1,2,3]
x is y
False
a[0] is ap[1]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a[0] is ap[1]
NameError: name 'ap' is not defined. Did you mean: 'a'?
a[0] is a[1]
False
b[0] is b[1]
True
