import turtle as tut

t = tut.Turtle()
s = tut.Screen()
s.bgcolor("Black")
t.pencolor("blue")
a = .5
while(True):
    t.forward(a)
    t.left(a)
    if(a == 27):
        break
    print(a)
    a += .5
t.hideturtle()
tut.done()