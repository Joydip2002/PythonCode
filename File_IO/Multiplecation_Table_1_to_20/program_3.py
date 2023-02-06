for i in range(1,21):
    with open(f"Multiplecation Table of {i}.txt",'w') as m:
        for j in range(1,11):
          m.write(f" {i} x {j} = {i * j} \n")
