num1 =float (input("Enter the first number: "))
op = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("Invalid operator")

print("The result is:", result)
