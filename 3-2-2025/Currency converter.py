def convert_currency(amount, rate=83.0):
    return amount * rate

usd = float(input("Enter amount in USD: "))
print(f"Equivalent in INR: {convert_currency(usd)}")
