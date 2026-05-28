def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

try:
    num1 = float(input("Enter the  first number "))
    operation = input("Enter the operation you want to perform ")
    num2 = float(input("Enter the second number "))

    result = eval(f"{num1}{operation}{num2}")  # eval() directly evaluates the mathematical expression as a string.

    print("ANSWER: ", result)

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

except SyntaxError:
    print("Invalid operation entered.")

except Exception as e:
    print("An error occurred:", e)

def addition():
    assert add(2,3) == 5
    assert add(5,3) == 8
    assert add (2,5) == 7
    assert add(8,9) == 17

def subtraction():
    assert sub(5,3) == 2
    assert sub(6, 5) == 1
    assert sub(8, 9) == -1
    assert sub(7, 4) == 3

def divison():
    assert divide(10,0) == "cannot divide by zero"
    assert divide(8,4) == 2
    assert divide(54,6) == 8
    assert divide(124,4) == 31

def multiplication():
    assert multiply(8,7) == 56
    assert multiply(5,9) == 45
    assert multiply(9867,0) == 0
    assert multiply(89,99) == 8811