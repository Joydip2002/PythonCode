f = open("another.txt","r")
data = f.read() 
f.close()

f2 = open("copy.txt","w")
f2.write(data)
f2.close