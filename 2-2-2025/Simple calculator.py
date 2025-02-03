while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
        else:
            result = "Invalid operation!"
        
        print("Result:", result)
    except ValueError:
        print("Invalid input!")
    
    if input("Do another calculation? (y/n): ").strip().lower() != 'y':
        break
