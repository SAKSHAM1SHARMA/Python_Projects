print("Calculator Menu")


def Add(a,b):
    return a+b

def Subtraction(a,b):
    return a - b

def Multiplication(a,b):
    return a*b

def Division(a,b):
    return a/b

while True:
    Menu_option = int(input("1.Add \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit \nEnter the option you want to calculate :"))
    if Menu_option == 5:
        print("You have successfully exited the Calculator.")
        break

    First_number = float(input("Enter the 1st number:"))
    Second_number = float(input("Enter the 2nd number:"))

    if Menu_option == 1:
        print("The Answer is ",Add(First_number,Second_number))

    if Menu_option == 2:
        print("The Answer is ",Subtraction(First_number,Second_number))

    if Menu_option == 3:
        print("The Answer is ",Multiplication(First_number,Second_number))

    if Menu_option == 4:
        if Second_number == 0 :
            print("You can't divide a number with 0.")
            break
        print("The Answer is ",Division(First_number,Second_number))

    

