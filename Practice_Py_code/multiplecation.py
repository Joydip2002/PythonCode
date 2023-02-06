def mulTable(n):
    if n <= 0:
        return n
    elif n >= 1:
      i = n
      for n in range(1,11):
          print(f"{n} x {i} = {n*i}")

Input = int(input("Enter Multiplecation Table Number: "))
mulTable(Input)