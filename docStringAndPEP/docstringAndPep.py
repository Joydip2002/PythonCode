# doc attribute (__doc__) for any of the Python objects and also with the built-in help() function.

# PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.
import colorama as color
def factorial(n):
  '''This is DocStrings. we Need to call __doc__ '''
  f = 1
  for i in range (1,n+1):
    f = f* i
  return f

print(factorial.__doc__)

n = int(input("Enter a Number: "))
print(color.Fore.GREEN+f"Factorial of {n} is: {factorial(n)}")