# f = open("Joydip.txt","w")
# WriteData = f.write("Just Checking File in Python")
# f.close()

n = input("Enter Searching Word: ")
f = open("Joydip.txt")
ReadData = f.read()

# f1 = open("Joydip.txt","a")
# appendData = f1.write("\nI am joydip manna")

if n in ReadData:
    print("Matched")
else:
    print("Not Matched")