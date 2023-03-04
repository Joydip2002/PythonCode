# def format_Number(x):
# #    print("{:,}".format(x))
#     s = str(x)
#     l = list(s)
#     # print(l)
#     count = 0
#     length = len(l)
#     # print(length)
#     for i in range(length):
#         # count = 0
#         # print(l[i])
#         if(l[i] == '0'):
#             count += 1

#         if(count == 3):
            
#             print(count)
#             l.insert(,',')
            
#     print("".join((l)))
    
# num = int(input("Enter Thousands Number: "))
# format_Number(num)


def format_number(n):
    if n < 0:
        raise ValueError("Number must be non-negative")
    number_string = str(n)
    # print(len(number_string))
    
    parts = []
    
    while number_string:
        parts.append(number_string[-3:]) 
        number_string = number_string[:-3]
        print(parts)
    formatted_string = ','.join(reversed(parts))
    return formatted_string


n = int(input("Enter Any Number: "))
print("\n\nFormatted Number is: ",format_number(n))