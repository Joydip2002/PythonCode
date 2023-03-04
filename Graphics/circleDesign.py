import turtle as t

a = t.Turtle()
s = t.Screen()
s.bgcolor("black")
a.color("yellow")
# a.speed(0)
c = 0
while True:
    if(c == 0):
        a.setheading(75)

    a.forward(120)
    a.left(145)

    if(c == 4):
        # a.forward(120)
        break;
    c += 1

 
a.hideturtle()
t.done()