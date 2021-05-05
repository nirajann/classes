def mysum(a,b):
    if type(a) is not int or type(b) is not int:
        raise TypeError("please enter the number")
    return a+b



a = "a"
b = 3
print(mysum(a,b))