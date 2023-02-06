student_1 = input("Enter Student_1 Name: ")
math_1 = int(input("Enter Math Number: "))
Phy_1 = int(input("Enter Physics Number: "))
Chem_1 = int(input("Enter Chemistry Number: "))
# student_2 = input("Enter Student_2 Name: ")
# math_2 = int(input("Enter Math Number: "))
# Phy_2 = int(input("Enter Physics Number: "))
# Chem_2 = int(input("Enter Chemistry Number: "))
s1_marks =((math_1+Phy_1+Chem_1)/300)*100
print(s1_marks)
# s2_marks =((math_2+Phy_2+Chem_2)/300)*100joy

if(s1_marks >= 40 or s1_marks == 33):
    print("PASS")
else:
    print("FAIL")