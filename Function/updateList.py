def updateList(l):
    l[2] = 38
    return l
l = [12,2,45,67,89]
print(id(l))
res = updateList(l)
print(res)
print(id(res))