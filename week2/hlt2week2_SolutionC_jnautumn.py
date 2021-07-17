year = 1
dep = 0.90
price= 2000
def bike(year,price,dep):
    while price >= 1000:
        price = price*dep
        year= year+1
        print("After", year, "years, your bike will be worth: ", price)
print("Starting price: " + str(price))
bike(year,price,dep)