import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.pencolor("green")    
turtle.circle(40, 80/2)
turtle.pencolor("yellow")
turtle.fd(40)
turtle.pencolor("red")  
turtle.circle(16, 180)
turtle.pencolor("black")
turtle.fd(40 * 2/3)
turtle.done()
