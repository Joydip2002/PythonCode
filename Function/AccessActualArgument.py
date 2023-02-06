# def details(*data):  # * => use for access all details
#     # print(name)
#     print(*data)

# details('Joydip',25,'974952637')

#When keyword use with actual data then use **
def details(**data):
    # print(name)
    # print(data)
    #we can print using for loop
    for i,j in data.items():
        print(i,j)

details(name = 'Joydip',age = 25, mob = '974952637')