import datetime as dt
import os
import time
import msvcrt  # For detecting keypress (Windows only)

os.system("cls")
print("Welcome to the Clock!")
print("Choose the format for the time display:")
print("1. 12-hour format (default)")
print("2. 24-hour format")
choice = int(input("Enter your choice (1 or 2): "))


print("Press 'q' to quit the clock.\n")

while True:
    now = dt.datetime.now()
    os.system("cls")
    
    if choice == 2:
        print("Current time:", now.strftime("%H:%M:%S"))
    else:
        print("Current time:", now.strftime("%I:%M:%S %p"))

    print("Date:", now.strftime("%Y-%m-%d"))
    print("Press 'q' to quit")

    time.sleep(1)

    # Check if a key is pressed
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key.lower() == b'q':
            break

print("Thank you for using the Clock!")
# Clear the console
os.system("cls")