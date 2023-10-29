import turtle as t

t.penup()
t.pendown()

t.fillcolor('yellow')
t.begin_fill()
for i in range(0,5):
    t.forward(96)
    t.right(144)
t.end_fill()

t.penup()
t.goto(100,-50)
t.pendown()
t.begin_fill()
for i in range(0,5):
    t.forward(32)
    t.right(144)
t.end_fill()
t.done()

