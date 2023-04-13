def fibonacci(n):
    """Returns a list of the first n Fibonacci numbers."""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

n = int(input("How many Fibonacci numbers do you want to generate? "))
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)
