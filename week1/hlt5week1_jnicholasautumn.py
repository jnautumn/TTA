title = "Python Mathbot"
print(title.upper())
print("Choose Two Numbers: ")
number_one = int(input("Number One: "))
number_two = int(input("Number Two: "))
def menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
menu()
option=int(input("Enter Option: "))
if option == 1:
    print("Result:")
    print(number_one + number_two)
elif option == 2:
     print("Result:")
     print(number_one - number_two)
elif option == 3:
     print("Result:")
     print(number_one * number_two)
elif option == 4:
     print("Result:")
     print(number_one / number_two)
elif option == 5:
     print("Result:")
     print(number_one ** number_two)
else: print("Invalid option")
print("Goodbye")
