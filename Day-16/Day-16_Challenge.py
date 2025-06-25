#-  Generate the first n Fibonacci numbers with a generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib = fibonacci(5)
for value in fib:
    print(value)
