def maxOfThree(a,b,c):
    if (a==b & a==c):
        print("All numbers are equal")
    elif (a>b):
        if(a>c):
            print(str(a)+" is Greater")
        else:
            print(str(c)+" is Greater")
    else:
        if(b>c):
            print(str(b)+" is Greater")
        else:
            print(str(c)+" is Greater")

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

maxOfThree(a,b,c)