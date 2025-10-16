# # Calculator
#
# num1 = float(input("Enter first number"))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number"))
#
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operator")
#

# Calculator from YouTube (python program to create calculator)
# Steps to create calculator
#     function for operation
#     user input
#     print

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def ave(num1, num2):
    return (num1 + num2) / 2


print("Please Select a operation:\n "\
      "1. Addition\n" \
      "2. Subtraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n")

select = int(input("Enter choice(1/2/3/4/5): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=", mul(num1, num2))
elif select == 4:
    print(num1, "/", num2, "=", div(num1, num2))
elif select == 5:
    print("Average of", num1, "and", num2, "is", ave(num1, num2))
else:
    print("Invalid input")
