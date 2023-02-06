def lengthChecking(l):
    length_5 = 0
    lengthOutOf_5 = 0
    for i in l:
        if(int(len(i)) == 5):
            length_5 = length_5 + 1
        else:
            lengthOutOf_5 = lengthOutOf_5 + 1
    return length_5,lengthOutOf_5

NameList = ["Joydip","Suman","Akash","Tanumoy","Ayan"]
# print(NameList)
res = lengthChecking(NameList)
print(res)