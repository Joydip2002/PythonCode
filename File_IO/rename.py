import os


with open("first.txt","r") as i:
    data = i.read()
with open("renamed_by_python.txt","w")as j:
    data1 = j.write(data)
    os.remove("first.txt")
    