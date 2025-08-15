import random
print("Welcome to the World of guessing numbers UwU")
computers_guess = random.randint(1,100)
users_input = 0
number_of_guess = 0
while(users_input!=computers_guess):
    users_input = int(input("Enter the Number you thing i have between 1 to 100:"))
    number_of_guess+=1

    if(users_input < computers_guess):
        print("You should aim for a higher number.")
    elif(users_input > computers_guess):
        print("Go with a smaller Numer.")
    else:
        print(f"Congrats you go me in {number_of_guess} attempts.")
