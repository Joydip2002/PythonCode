import turtle as tut

t = tut.Turtle()
s = tut.Screen()
s.bgcolor("black")
t.pencolor("white")

t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()

a = 0
b = 0
while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if(b == 200):
        break




tut.done()