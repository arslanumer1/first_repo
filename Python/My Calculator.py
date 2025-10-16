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

# Calculator to convert miles into kilometer and vice versa

def miles_to_kilometer(miles):
    return miles * 1.60934


def kilometer_to_miles(kilometers):
    return kilometers / 1.60934


while True:
    print("Hello! Miles to kilometer calculator\n " \
          "1. Miles to Kilometer\n " \
          "2. Kilometer to Miles\n " \
          "3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        miles = float(input("Enter a number of miles: "))
        print (f"{miles} miles is {miles_to_kilometer(miles)} kilometer")
    elif choice == 2:
        kilometers = float(input("Enter a number of kilometers: "))
        print (f"{kilometers} kilometers is {kilometer_to_miles(kilometers)} miles")
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid input")

