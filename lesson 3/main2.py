num= int(input("enter number to check:"))
if num>50:
    print("number is greater than 50")
    if num%2==0:
        print("and its even too")
    else:
        print("and its odd")
else:   
    print("number is less than 50")