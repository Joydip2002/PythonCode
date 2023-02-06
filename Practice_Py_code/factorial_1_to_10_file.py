import math
for i in range(1,11):
    with open(f"Facttorial-{i}.txt","w") as m:
        s = math.factorial(i)
        m.write(str(s))