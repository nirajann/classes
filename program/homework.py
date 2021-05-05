a = 64
for i in range(5):
    for j in range(i):
        a += 1
        print (chr(a),end=" ")
    print()

print("""
""")

d = 64
for i in range(6):
    for j in range(4-i):
        d += 1
        print (chr(d),end=" ")
    print()


print("""
""")
b = 63
for i in range(0,5):
    b += 1
    for j in range(i):
        print (chr(b),end=" ")


    print()

print("""
""")

e = "*"
for i in range(5,1,-1):
        for j in range(i-1):
            print(e, end=" ")
        print()

print("""
""")

for i in range(6,1,-1):
        for j in range(1,i-1):
            print(j, end=" ")
        print()