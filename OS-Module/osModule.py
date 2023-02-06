import os
#Create Directory
if (not os.path.exists("OS-Module/data")):
    os.mkdir("OS-Module/data")
# for i in range(1,101):
#  os.mkdir(f"OS-Module/data/day{i}")

#Rename Directory
for i in range(1,101):
    os.rename(f"OS-Module/data/Tuto {i}",f"OS-Module/data/Tutorial {i}")