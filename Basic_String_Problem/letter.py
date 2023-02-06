letter = '''Dear |<NAME>|,
\tYou Are Selected!
\tThank You Dear
Regurds 
Joydip
<|DATE>|
'''
name = input("Enter Your Name: ")
date = input("Enter Date: ")
letter = letter.replace("|<NAME>|", name)
letter = letter.replace("<|DATE>|", date)
print(letter)