print("Welcome!")
print("Let's start your order with a classic hamburger!")
burger = 1.25
fries = input("Add Fries? Y/N: ")
fries = fries.upper() #force input to uppercase regardless of user input to prevent output error(s)
if fries == "Y":
    num1 = 1.10
    num2 = burger + num1
drink = input("Add a Drink? Y/N: ")
drink = drink.upper()
if drink =="Y" and fries == "Y":
    num3 = 0.99
    num4 = num2 + num3
    print ("Your total is: " + str(num4))
elif fries == "N" and drink == "Y":
    num3 = 0.99
    num5= burger + num3
    print ("Your total is: " + str(num5))
elif drink == "N" and fries == "Y":
    print("Your total is: " + str(num2))
elif drink != "Y" or "N" and fries != "Y" or "N": #user must input y/n to yield output
    error = "Input error! Try again!"
    error = error.upper()
    print(error)
else: print("Your total is: " + str(burger))
print("Thank you!")