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

# # Calculator to convert miles into kilometer and vice versa
#
# def miles_to_kilometer(miles):
#     return miles * 1.60934
#
#
# def kilometer_to_miles(kilometers):
#     return kilometers / 1.60934
#
#
# while True:
#     print("Hello! Miles to kilometer calculator\n " \
#           "1. Miles to Kilometer\n " \
#           "2. Kilometer to Miles\n " \
#           "3. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 1:
#         miles = float(input("Enter a number of miles: "))
#         print (f"{miles} miles is {miles_to_kilometer(miles)} kilometer")
#     elif choice == 2:
#         kilometers = float(input("Enter a number of kilometers: "))
#         print (f"{kilometers} kilometers is {kilometer_to_miles(kilometers)} miles")
#     elif choice == 3:
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid input")

#Calculator to convert Fahrenheit into celsius and vice versa

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

while True:
    print("Hello! Fahrenheit to celsius calculator\n " \
          "1. Fahrenheit to Celsius\n " \
          "2. Celsius to Fahrenheit\n " \
          "3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Fahrenheit to Celsius")
        fahrenheit = float(input("Enter a number of Fahrenheit: "))
        print(f"{fahrenheit} Fahrenheit is {fahrenheit_to_celsius(fahrenheit)} Celsius")
    elif choice == 2:
        print("Celsius to Fahrenheit")
        celsius = float(input("Enter a number of Celsius: "))
        print(f"{celsius} Celsius is {celsius_to_fahrenheit(celsius)} Fahrenheit")
    elif choice == 3:
        print("Goodbye!")
        break
    else: print("Invalid input, please try again")