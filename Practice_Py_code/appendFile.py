#--------Write File---------
# f = open("abc.txt","w")
# writeFile = f.write("My Name Is Joydip Manna")
# print(writeFile)
# f.close()

#-------Append Data---------
# f = open("abc.txt","a")
# appendFile = f.write("\n I am From West Bengal")
# print(appendFile)
# f.close()

#------Read Data------------
# f = open("abc.txt","r")  # r => Read Data by default
# ReadData = f.read()

# print(ReadData)

#------ReadLine------
f = open("abc.txt")

data = f.readlines()
print(data)
# data = f.readline()
# print(data)



