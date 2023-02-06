from array import *

#Selection Sort
def selectionSort(data,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(data[i] > data[j]):
                temp = data[i]
                data[i] = data[j]
                data[j] = temp

#Bubble Sort
def bubbleSort(data,n):
    counter = 1
    while(counter < n):
        for j in range(0,n-counter):
            if(data[j] > data[j+1]):
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
        counter += 1

#Insertion Sort

def insertionSort(data,n):
    for i in range(1,n):
        current = data[i]
        j = i-1
        while(data[j] > current and j >= 0):
            data[j+1] = data[j]
            j -= 1
        data[j+1] = current


#Printing
def printing(data,n):
    for i in range(n):
        print(data[i])


n = int(input("Enter Size of N: "))
data = array('i',[])
no=1
for i in range(n):
    x = int(input(f"Enter {no} Array Element: "))
    data.append(x)
    no+=1

# print(data)
# selectionSort(data,n)
# bubbleSort(data,n)
insertionSort(data,n)
printing(data,n)