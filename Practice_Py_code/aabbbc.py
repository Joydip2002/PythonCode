s = "aabbbc"
li = list(s)
l = len(li)
aCount = 0
bCount = 0
cCount = 0
# print(li[0])

for i in range(l):
    if(li[i] == 'a'):
        aCount += 1
    elif(li[i] == 'b'):
        bCount += 1
    else:
        cCount += 1

print(f"a{aCount}b{bCount}c{cCount}")

