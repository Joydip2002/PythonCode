# f1 = open("1.txt","a")
# appendData = f1.write("This is file 1.txt")
# print(appendData)
# f1.close()

# f2 = open("2.txt","a")
# appendData = f2.write("This is file 1.txt")
# print(appendData)
# f2.close()

f1 = open("1.txt")
f1_Data = f1.read()

f2 = open("2.txt")
f2_Data = f2.read()

if f1_Data == f2_Data:
    print ("File Content Matched")
else:
    print("File Content Mismatched!")
