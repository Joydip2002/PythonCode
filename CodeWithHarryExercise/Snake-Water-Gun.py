import random
from colorama import Fore,Back,Style
user_Name = input("Enter Your Name: ")
game_Component = ["snake","water","gun"]
n = int(input("How Many Round Play (Like 5,10,etc): "))
count = 1
while(n):
    user_Data = input(f"{count}: Enter (Snake/Water/Gun) Your Choice: ")
    lowerCase_User_data = user_Data.lower()
    # print(lowerCase_User_data)
    computer_Data = random.choice(game_Component)
    print("Computer Choose: ",computer_Data)

    if(lowerCase_User_data == computer_Data):
        print(Fore.YELLOW+"Draw",end="\n")
    elif((computer_Data == "snake" and lowerCase_User_data == "water") or (computer_Data == "water" and lowerCase_User_data == "gun") or (computer_Data == "gun" and lowerCase_User_data == "snake")):
        print(Fore.GREEN+"Computer Win!",end="\n")
    elif((computer_Data == "water" and lowerCase_User_data == "snake") or (computer_Data == "gun" and lowerCase_User_data == "water") or (computer_Data == "snake" and lowerCase_User_data == "gun")):
        print(Fore.GREEN+f"{user_Name} Win!")
    else:
        print("Incorrect Data!")
    n -= 1
    count += 1