list1 = [1,2,3]

list2 = list1.copy()
list2.reverse()
print(list2)

if list1 == list2:
    print("Palindrome")
else:
    print("Not Palindrome")