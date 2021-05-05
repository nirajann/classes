"""
WAP to check a number given by the user is a armstrong or not
"""

num = int(input("write any number"))
a=num
sum = 0

while num > 0:
    rem = num % 10
    sum = sum + (rem**3)
    num = num // 10


if a== sum:
    print("this is arm")
else:
    print("error")


