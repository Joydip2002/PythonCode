file1 = "section1.txt"
file2 = "section2.txt"
with open(file1,"r") as i:
    data1 = i.read()
with open(file2,"r") as j:
    data2 = j.read()
if data1 == data2:
    print("Two File Is Identical")
else:
    print("Two File is Not Identical")

