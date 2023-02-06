name = (input("Enter A Name: "))
print(name)
# length = name.__len__()
length = len(name)
print(type(length))

if(length < 10):
    print("Less then 10 character is available")
elif(length == 10):
    print("Equal Charectersis available")
else:
    print("More then 10 character is available")
