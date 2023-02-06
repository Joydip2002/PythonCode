# from typing import Match


f = open("sample.txt","r")
data = f.read()
print(data)
n = input("Enter A Word: ")
if n in data:
    print("Word Match")
else:
   print("Word Not Match")