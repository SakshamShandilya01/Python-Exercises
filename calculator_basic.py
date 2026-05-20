num1 = float(input("Enter the  first number "))
operation = input("Enter the operation you want to perform ")
num2 = float(input("Enter the second number "))

result = eval(f"{num1}{operation}{num2}") # eval() directly evaluates the mathematical expression as a string.

print("ANSWER: ", result)