Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
oh = [1,2,3,4,5]
for i in range(len(oh)):
    oh[i] = oh[i] * 2

    
oh
[2, 4, 6, 8, 10]
x = [i for i in range(10)]
x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [i+1 for i in range(10)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oh
[2, 4, 6, 8, 10]
oh = [1,2,3,4,5]
oh = [i * 2 for i in oh]
oh
[2, 4, 6, 8, 10]
x [ ]
SyntaxError: invalid syntax
x= []
for i in range(10):
    x.append(i+1)

    
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [c * 2 for c in 'Fishc']
y
['FF', 'ii', 'ss', 'hh', 'cc']
code = [ord(c) for c in 'fich']
code
[102, 105, 99, 104]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
col2 = [row(1) for row in matric]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    col2 = [row(1) for row in matric]
NameError: name 'matric' is not defined. Did you mean: 'matrix'?
col2 = [row(1) for row in matrix]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    col2 = [row(1) for row in matrix]
  File "<pyshell#27>", line 1, in <listcomp>
    col2 = [row(1) for row in matrix]
TypeError: 'list' object is not callable
col2 = [row[1] for row in matrix]
col2
[2, 5, 8]
col2 = [i for i in matrix]
col2
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [line[1] for line in matrix]
col2
[2, 5, 8]
diag = [matrix[i][i] for i in range(len(matrix))]
diag
[1, 5, 9]
line = [matrix[i][len(matrix) -1 -i] for in range(len(matrix))]
SyntaxError: invalid syntax
line = [matrix[i][len(matrix) -1 -i] for i in range(len(matrix))]
line
[3, 5, 7]
line = [matrix[-i][-i] for i in range(len(matrix))]
line
[1, 9, 5]
line = [matrix[1-i][i] for i in range(len(matrix))]
line
[4, 2, 9]
line = [matrix[-1][-i] for i in range(len(matrix))]
line
[7, 9, 8]
line = [matrix[1][i] for i in range(len(matrix))]
line
[4, 5, 6]
b = [[0]*3] * 3
\
b
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b[1] = 1
b
[[0, 0, 0], 1, [0, 0, 0]]
b[1][1] = 1
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    b[1][1] = 1
TypeError: 'int' object does not support item assignment
b = [[0]*3] * 3
b
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b[1][1] = 1
b
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
a = [0] * 3
for i in range(3):
    a[i] = [0]*3

    
a
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  s = [i for i in range(10) if i % 2 == 0]
  
SyntaxError: unexpected indent
s = [i for i in range(10) if i % 2 == 0]
s
[0, 2, 4, 6, 8]
words = ['great','fishc','brilinat','excellent','fantistic']
words = [i for i in words if i[0] ='f']
SyntaxError: invalid syntax
words = [i for i in words if i[0] == 'f']
words
['fishc', 'fantistic']
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
fla = [col for row in matrix for col in row]
fla
[1, 2, 3, 4, 5, 6, 7, 8, 9]
fla = [row for row in matrix]
fla
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  [[x,y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
  
SyntaxError: unexpected indent
[[x,y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
[[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6], [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]
