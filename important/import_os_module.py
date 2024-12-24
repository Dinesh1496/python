import os

print(os.getenv("apitoken"))

password = (os.getenv("password"))


a= 3//2
print(a)

b = 2
b += 6

print(b)

c = 10
c -= b
print(c)

#identity operator
x= 10
y =11

if x is y:
    print("true")
if x is not y:
    print("false")

