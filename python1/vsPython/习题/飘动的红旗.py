import turtle as t
t.penup()
t.goto(-100,200)
t.pendown()

t.pensize(9)
t.right(90)
t.forward(400)
t.fillcolor('red')

t.penup()
t.goto(-100,200)
t.pendown()
t.begin_fill()
t.left(115)
t.circle(-200,55)
t.circle(200,55)
t.right(115)
t.forward(200)
t.right(65)
t.circle(-200,55)
t.circle(200,55)
t.end_fill()

t.done()