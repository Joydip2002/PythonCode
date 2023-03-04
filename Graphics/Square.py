import turtle as t

a = t.Turtle()
s = t.Screen()

a.color("blue")
s.bgcolor("black")
c = 0

for i in range (100):
    a.forward(100-c)
    a.left(90)
    c += 3

t.done()