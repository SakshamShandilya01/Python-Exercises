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