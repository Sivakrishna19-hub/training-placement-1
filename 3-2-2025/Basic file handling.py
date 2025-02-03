def write_to_file():
    with open("user_data.txt", "w") as file:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        file.write(f"Name: {name}\nAge: {age}\n")

def read_from_file():
    try:
        with open("user_data.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found!")

while True:
    print("\n1. Write to file\n2. Read from file\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        write_to_file()
    elif choice == "2":
        read_from_file()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
