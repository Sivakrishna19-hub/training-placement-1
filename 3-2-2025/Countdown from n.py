def countdown(n):
    while n > 0:
        print(n, end=" ")
        n -= 1
    print("Blast Off!")

countdown_num = int(input("Enter a number for countdown: "))
countdown(countdown_num)
