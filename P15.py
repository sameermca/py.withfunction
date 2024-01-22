# Write a Python program to find Factorial of a Number.

def fact(n):
    f = 1
    if n < 0:
        print("Factorial does not Exist for Negative Numbers")
    elif n == 0:
        print("The Factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            f = f * i
        print("The Factorial of",n,"is",f) 

num = int(input("Enter a Number :-\n"))
fact(num)