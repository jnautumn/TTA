def bike(x):
    print(x)
    if x<=1000:
        return x
    else:
        bike(x*0.90) #Recursive call?
bike(2000)