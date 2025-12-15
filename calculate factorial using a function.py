def fact(num):
    if num==1:
       return 1
    else:
        factorial=num*fact(num-1)
        return factorial

x=int(input("Enter a no: "))
if x>=1:
    fact(x)
    print(f" The factorial of {x} is {fact(x)}")
else:
    print("Invalid entry.Enter a no greater than 0")
