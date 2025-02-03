def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(ord(char) + shift_amount) if char.islower() else chr(ord(char) + shift_amount)
            result += new_char if new_char.isalpha() else chr(ord(char) + shift_amount - 26)
        else:
            result += char
    return result

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

print("Encrypted:", caesar_cipher(message, shift))
