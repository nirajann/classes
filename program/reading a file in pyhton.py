#reading a file from pyhton

f = open("test.txt",'r')
content = f.read()
print(content)
print(type(content))
f.close()