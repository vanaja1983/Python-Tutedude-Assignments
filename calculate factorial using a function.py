def fact(num):
    if num==1:
       return 1
    elif num<=0:
       print("Invalid entry.Enter a no greater than 0")
       return None
    else:
        factorial=num*fact(num-1)
        return factorial

x=int(input("Enter a no: "))
fact(x)
print(f" The factorial of {x} is {fact(x)}")



