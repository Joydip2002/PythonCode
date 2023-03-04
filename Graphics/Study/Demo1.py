import turtle as t

arrow = t.Turtle()
s = t.Screen()
s.bgcolor("black") #ScreenColor


# print(t.shape())     'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
# print(help(t.shape))
arrow.speed(1)
    # 'fastest' : 0
    # 'fast' : 10
    # 'normal' : 6
    # 'slow' : 3
    # 'slowest' : 1
arrow.color("blue")
arrow.forward(100)
arrow.color("red")  #Cursor Color

t.done()
