my_list=([3,45,83])
numbers= open("Numbers.txt","w")
for i in range(1):
    numbers.write(str(my_list))
    numbers.write("\n")
numbers.close()
add= ([21])
add=(my_list + add)
numbers= open ("Numbers.txt","a")
numbers.write(str(add))
numbers.write("\n")
numbers.close()
numbers= open ("Numbers.txt", "r")
print (numbers.read())
numbers.close()