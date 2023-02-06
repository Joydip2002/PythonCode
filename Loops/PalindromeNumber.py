def palindromeFunc(n):
   s = 0 
   while n > 0:
    rem = n % 10
    s = s*10 + rem
    n = int(n/10)
   return s

n = int(input("Enter A Number: "))
rev = palindromeFunc(n)
print(rev)

if n == rev:
    print("Palindrome Number")
else:
    print("Non-Palindrome Number")