def login_system():
    # Pre-loaded with a sample user
    users = {"admin": "password123"}

    while True:
        print("\n--- User Login System ---")
        print("1. Register New User")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            username = input("Enter a new username: ")
            if username in users:
                print("❌ Username already exists! Please choose another.")
            else:
                password = input("Enter a password: ")
                users[username] = password
                print("✅ Registration successful! You can now log in.")

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            # Check if username exists and password matches
            if username in users and users[username] == password:
                print(f"🎉 Login successful! Welcome back, {username}.")
            else:
                print("❌ Invalid username or password. Please try again.")

        elif choice == "3":
            print("Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    login_system()