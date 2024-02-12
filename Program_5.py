def countUpperLower(a):
    upper_count = 0
    lower_count = 0
    
    for i in a:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    
    return upper_count, lower_count

a = input("Enter a string: ")
upper, lower = countUpperLower(a)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)