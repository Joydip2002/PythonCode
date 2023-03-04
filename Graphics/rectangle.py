import turtle as t

a = t.Turtle()
s = t.Screen()
a.color("blue")
s.bgcolor("black")
c = 1
while True:
    if(c == 1):
        a.forward(100)
        a.left(90)
        a.forward(75)
    else:
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(75)
        break
    c += 1


a.hideturtle()
t.done()