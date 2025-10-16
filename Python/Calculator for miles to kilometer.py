print("Hello! Miles to kilometer calculator")
type_of_calc = input("Enter 'm' for miles to kilometer or 'k' for kilometer to miles: ")

if type_of_calc == "m":
    answer = float(input("Enter a number of miles: "))
    print(f"{answer} miles is {answer * 1.60934} kilometer")
elif type_of_calc == "k":
    answer = float(input("Enter a number of kilometer: "))
    print(f"{answer} kilometer is {answer / 1.60934} miles")
else:
    print("Invalid input")