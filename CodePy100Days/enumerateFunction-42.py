# Enumerate function: Enumerate function is used for provides index corresponding the elements.And you can set start position
# enumerate(li)
# enumerate(li, start = 3)

li = [12,4,34,45,65]

for index, value in enumerate(li,start=3):
    print(index,value)
