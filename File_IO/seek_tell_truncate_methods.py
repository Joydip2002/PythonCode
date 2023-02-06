# f = open("seekTell.txt","w")
# data = f.write("I am A Bad Boy")
# print(data)
# # f.close()



# f = open("seekTell.txt","r")
# f.seek(5) # Avoid First Five letter 
# print(f.tell())  #tell how many data seek
# data = f.read()
# print(data)

f = open("seekTell2.txt","w")
data = f.write("Hello World")
f.truncate(5)