def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

while True:
    choice = input("Enter 1 to convert binary to decimal or 2 to convert decimal to binary (or 'exit' to quit): ")

    if choice == "1":
        binary = input("Enter binary number: ")
        print(f"Decimal: {binary_to_decimal(binary)}")
    elif choice == "2":
        decimal = int(input("Enter decimal number: "))
        print(f"Binary: {decimal_to_binary(decimal)}")
    elif choice == "exit":
        break
    else:
        print("Invalid choice!")
