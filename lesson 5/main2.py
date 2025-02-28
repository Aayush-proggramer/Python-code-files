def refactorial(n):
    if n==1 or n==0:
       return 1
    else:
     return n*refactorial(n-1)

num = int(input('enter a number'))
if num < 0:
    print('sorry factorial dosent exist for negative numbers')
else:
    print("the factorial of", num, "is ", refactorial(num))