def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n_terms = int(input("Enter number of terms: "))
fibonacci(n_terms)
