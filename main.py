import random
import string
from getpass import getpass
from database import add_password, view_passwords, search_password, delete_password,update_password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ""

    for i in range(12):
        password += random.choice(characters)

    return password
while True:
    print("=" * 40)
    print("        🔐 PASSWORD MANAGER")
    print("=" * 40)
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Generate Password")
    print("6. update password")
    print("7. Exit")

    choice = input("choose a option  from (1-7): ")

    if choice == "1":
        website = input("Website: ")
        username = input("Username: ")

        choice = input("Generate password automatically? (y/n): ")

        if choice.lower() == "y":
            password = generate_password()
            print("Generated Password:", password)
        else:
            password = getpass("Password: ")

        add_password(website, username, password)

    elif choice == "2":

        data = view_passwords()

        print("\nSaved Passwords\n")

        print("-" * 60)
        print(f"{'ID':<5}{'Website':<20}{'Username':<20}{'Password'}")
        print("-" * 60)

        for row in data:
            print(f"{row[0]:<5}{row[1]:<20}{row[2]:<20}{row[3]}")

    elif choice == "3":

        website = input("Enter website: ")

        result = search_password(website)

        if result:
            print("\nFound Password(s):")
            for row in result:
                print(row)
        else:
            print("No password found.")
    elif choice=="4":
        id=input("Enter ID to delete:")
        delete_password(id)

    elif choice == "5":

        print("\nGenerated Password")
        print(generate_password())
    elif choice == "6":
        id = input("Enter ID to update: ")

        website = input("New Website: ")
        username = input("New Username: ")

        ch = input("Generate new password? (y/n): ")

        if ch.lower() == "y":
            password = generate_password()
            print("Generated Password:", password)
        else:
            password = getpass("New Password: ")

        update_password(id, website, username, password)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")