"""square = {}

for x in range(11):
    if x % 2 == 1:
      square[x] = x*x

print(square)"""




def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    print(product)


#recurssion example
def fact(alu):
    if alu ==1 or alu == 0:
        return 1
    else:
        return alu*fact(alu-1)

print(fact(5))