print("-------❤️  Calculator ❤️------\nOperations are:~~~ ")
opList = ["+","-","*","/","%"]
print(opList)
while(True):
    fn = int(input("Enter First Number: "))
    sn = int(input("Enter Second Number: "))
   
    op = input("Enter Operation: ")

    match op:
            case "+" :
                sum = fn + sn;
                print(sum)
            case "-" :
                sub = fn -sn
                print(sub)
            case "*" :
                mul = fn * sn;
                print(mul)
            case "/" :
                div = fn/sn;
                print(div)
            case "%":
                mod = fn % sn;
                print(mod)
            case _ if(fn+sn == 20):
                print("if Statement")
            case _:
                print("Wrong Choice!")
                
