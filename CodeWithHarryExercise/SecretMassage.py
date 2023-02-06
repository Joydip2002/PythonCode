# # Write a python program to translate a message into secret code
# language. Use the rules below to translate normal English into secret
# code language

# # Coding:
# # if the word contains at least 3 characters, remove the first letter
# and append it at the end
# now append three random characters at the starting and the end
# else:
# simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last
# tetter and append it to the beginning
import random as rand
import string
str_any = input("Enter Your Secret Code: ")
li = list(str_any)
f = 3
#---------Start Encoding--------------
if(len(li)>=3):
    remove_letter = li.pop(0)
    li.append(remove_letter)
    # print(li)
    while(f > 0):
        insertFirst = li.insert(0,''.join(rand.choice(string.ascii_lowercase)))
        insertLast = li.append(''.join(rand.choice(string.ascii_lowercase)))
        f -=1
    # print(li)
    encode_str = ''.join(map(str,li))
else:
    li.reverse()
    encode_str = ''.join(map(str,li))
print("After Encoding Data is: ",encode_str)
#---------end Encoding-------------------

# ---------------Decoding----------------
li_decode = list(encode_str)
n = len(li_decode) 
# print(n)
check = 3
while(n > check and check > 0):
    li_decode.pop(n-1) 
    n -= 1
    check -= 1
# print(li_decode)

checkFirst = 3
firstRemove = 0
while(checkFirst> 0):
    li_decode.pop(firstRemove)
    checkFirst -= 1

# print(li_decode)

l_idx = len(li_decode)
li = li_decode.pop(l_idx-1)
# print(li)
final_decode_str = li_decode.insert(0,li)
print("After Decoding : ",''.join(map(str,li_decode)))
