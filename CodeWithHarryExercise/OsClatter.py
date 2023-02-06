import os
# Create txt File
# if(not os.path.exists("CodeWithHarryExercise/Data")):
#     os.mkdir("CodeWithHarryExercise/Data")

# for i in range(0,50):
#     f = open(f"CodeWithHarryExercise/Data/Pic{i+1}.png","w")
#     f.close()

allImage = os.listdir("CodeWithHarryExercise/Data")

totalImage = len(allImage)
li = list(allImage)
print(li)

print("If You Rename Write : 'r'")
un = input("Enter Your Input: ")
match(un):
    case "r":
        for i in range(len(li)):
            print(f"CodeWithHarryExercise/Data/{li[i]}")
            os.rename(f"CodeWithHarryExercise/Data/{li[i]}",f"CodeWithHarryExercise/Data/RenameFile{li[i]}.png")
    case _:
        print("Wrong Input")