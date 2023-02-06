def game(s):
    return s

a = input("Enter Score")

score = game(a)

with open("another_1.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':
    with open("another_1.txt", "w") as f:
        f.write(str(score))

elif hiScoreStr<score :
    with open("another_1.txt", "w") as f:
        f.write(str(score))