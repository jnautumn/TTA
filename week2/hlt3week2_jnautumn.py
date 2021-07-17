title = "Python Mathbot V2"
print(title.upper())
print("jnautumn 17/07/21")
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
def add(number_one,number_two):
    result= number_one + number_two
    print(number_one, "+", number_two, "= ", result)
def subtract(number_one,number_two):
    result= number_one - number_two
    print(number_one, "-", number_two, "= ", result)
def multiply(number_one,number_two):
    result = number_one * number_two
    print(number_one, "X", number_two, "= ", result)
def divide(number_one,number_two):
    result = number_one / number_two
    print(number_one, "/", number_two, "= ", result)
def square(number_one,number_two):
    result=number_one ** number_two
    print(number_one, "^", number_two, "= ", result)
if option== 1:
    add(number_one,number_two)
elif option== 2:
    subtract(number_one,number_two)
elif option== 3:
    multiply(number_one,number_two)
elif option== 4:
    divide(number_one,number_two)
elif option== 5:
    square(number_one,number_two)
else: print("Invalid Option")
print("Goodbye!")