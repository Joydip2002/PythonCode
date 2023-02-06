name = "\nWelcome To Kon Banega Crore Pati"
print(name.upper().center(50))
print("~~~~~~~~~~~~~~~~Rule~~~~~~~~~~~~~~~~\n1.There are Five question.\n2.Each Question Price is 5000\n3.Negative Deducation Price: 2000")
question = ["Who is Prime Minister","What is Full form of ATM","Father Of Python","How Much Color in National Flag","Make Directory Command in Linux"]
print()
# print(len(question)) 

n = len(question)
totalEarn = 0

for i in range(n):
    q1 = input(f"Question:{i+1}. {question[i]} : ")
    qindex = question.index(question[i])
    # print(qindex)
    if((q1.upper() == "NARENDRA DAMODARDAS MODI" and qindex == 0 ) or (q1.upper() == "AUTOMATED TELLER MACHINE" and qindex == 1) or (q1.upper() == "GUIDO VAN ROSSAM" and qindex == 2) or (q1.upper() == "3" and qindex == 3) or (q1.upper() == "MKDIR" and qindex == 4)):

        print("Correct Answer")
        totalEarn += 5000
    
    else:
        print("Incorrect Answer")
        if(totalEarn >= 2000 ):
            totalEarn -= 2000
        else:
            totalEarn = 0

    print("\nYour Earnings : ",totalEarn)
    if(i < n-1):
        print("--------Next Question-------")
    else:
        print("========End Round======")
    
    

