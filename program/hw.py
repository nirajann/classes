# write a program to find the factorial of program by using function
"""
write a program to print a multiplication of table of a given number by using the function
"""
def factorial(num):
    fac = 1
    for i in range(1, num + 1):
        fac = fac * i
    return fac

num = 5
x = factorial(num)
print(x)

def multiplication(num):
    for i in range(1, 11):
        mul = num * i
        print(f"{num} * {i} = {mul}")


num = int(input("enter the number"))
multiplication(num)