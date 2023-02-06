a = [1,2,3,4,"joy",34.4,'c']
print(a)
# access list Element by index
b = a[2]
print(b)
# update by value
a[4] = "Barsha"
print(a)
# list slicing
s = a[:5]     #-->0 to 4 or write a[0:5]
print(s)
s1 = a[3:]    #--->here starting value is 4 and ending value is c, Or write a[3:7]
print(s1)

# Negative Indexing
s2 = a[-7:-1]
print(s2)