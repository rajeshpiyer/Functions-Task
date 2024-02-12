def sum(a,b):
    return a+b

def difference(a,b):
    if a<b:
        return b-a
    else:
        return a-b
    
def product(a,b):
    return a*b

def quotient(a,b):
    return a/b

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
print("Sum = ",sum(a,b))
print("Difference = ",difference(a,b))
print("Product = ",product(a,b))
print("Quotient = ",quotient(a,b))
