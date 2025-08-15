import msvcrt

CREDENTIALS_LENGTH = 30
MAX_USERS = 10

users = {}

def input_password_masked(prompt="Enter password: "):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = msvcrt.getch()
        if char in {b'\r', b'\n'}:  # Enter key
            print()  # Move to next line
            break
        elif char == b'\x08':  # Backspace
            if len(password) > 0:
                password = password[:-1]
                print('\b \b', end="", flush=True)
        elif char in {b'\x00', b'\xe0'}:
            msvcrt.getch()  # Ignore special keys
        else:
            try:
                decoded = char.decode('utf-8')
                password += decoded
                print('*', end="", flush=True)
            except UnicodeDecodeError:
                pass
    return password

def register_user(username, password):
    username = username.strip()
    password = password.strip()

    if not username or not password:
        raise ValueError("Username and password cannot be empty.")
    
    if len(username) > CREDENTIALS_LENGTH or len(password) > CREDENTIALS_LENGTH:
        raise ValueError("Username or password exceeds maximum length.")
    
    if not username.isalnum():
        raise ValueError("Username must be alphanumeric.")
    
    if username in users:
        raise ValueError("Username already exists.")
    
    if len(users) >= MAX_USERS:
        raise ValueError("Maximum number of users reached.")
    
    users[username] = password
    print(f"User '{username}' registered successfully.")

def login_user(username, password):
    username = username.strip()
    password = password.strip()

    if len(username) > CREDENTIALS_LENGTH or len(password) > CREDENTIALS_LENGTH:
        raise ValueError("Username or password exceeds maximum length.")
    
    if username not in users or users[username] != password:
        raise ValueError("Invalid username or password.")
    
    print(f"User '{username}' logged in successfully.")

# Main loop
while True:
    print("\n--- User Menu ---")
    print("1. Register User")
    print("2. Login User")
    print("3. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        username = input("Enter username: ")
        password = input_password_masked("Enter password: ")
        try:
            register_user(username, password)
        except ValueError as e:
            print("Error:", e)
    
    elif choice == '2':
        username = input("Enter username: ")
        password = input_password_masked("Enter password: ")
        try:
            login_user(username, password)
        except ValueError as e:
            print("Error:", e)
    
    elif choice == '3':
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice, please try again.")
