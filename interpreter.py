expression = input("Enter a math expression: ")
x,y,z = expression.split(" ")
x = int(x)
z = int(z)

if y == "+":
    print(x + z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x * z)
elif y == "/" and z != 0:
    print(x/z)
elif y == "/" and z == 0:
    print("Cannot divide by zero")
else:
    print("Invalid operator")
