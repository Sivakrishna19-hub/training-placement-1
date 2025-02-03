num = int(input("Enter a number: "))
digits = [int(digit) for digit in str(num)]
sum_of_powers = sum(digit ** len(digits) for digit in digits)

print(f"{num} is an Armstrong number" if sum_of_powers == num else f"{num} is not an Armstrong number")
