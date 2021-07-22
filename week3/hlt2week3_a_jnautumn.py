grade = int(input("Enter Your Grade: " + "%"))
def mark_grade():
    if grade <= 50:
        print(grade, "= U")
    elif grade <= 60:
        print(grade, "= D")
    elif grade <= 70:
        print (grade, "= C")
    elif grade <=80:
        print (grade, "= B")
    elif grade <=90:
        print (grade, "= A")
    elif grade <=100:
        print (grade, "= A*")
    else:
        print ("Invalid Input")
mark_grade()
#Extension tba: