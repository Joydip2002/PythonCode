# f = open("sample.txt","r") # "r" means read.It Is optional,by default access "r"
f = open("sample.txt")
data = f.read()
print(data)
f.close()