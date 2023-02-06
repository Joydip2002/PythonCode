with open("sample2.txt") as f:
    data = f.read()
    print(data)
    data = data.replace("Donkey","######")
    with open("sample2.txt","w") as f:
        f.write(data)
         