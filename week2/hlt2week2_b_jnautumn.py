dep = 0.90
def bike(price,dep):
    print(int(price))
    while price>1000:
        price=price*dep
        print(int(price))
    if price<1000:
        print("complete")
bike(2000,dep)