def primeOrNot(a):
    flag=0
    for i in range (2, (a//2+1)):
        if a % i == 0:
            flag=1
            break
    if flag==0:
        print("The number "+str(a)+" is Prime!!")
    else:
        print("The number "+str(a)+" is not Prime!!")

a = int(input("Enter a number : "))
primeOrNot(a)