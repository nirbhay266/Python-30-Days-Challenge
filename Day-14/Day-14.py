#Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Example usage
print("Factorial of 5 is:", factorial(5))  # Output: 120

#fibonasice series
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
# Example usage
print("Fibonacci series of 10 terms:", fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#Example:-                                 
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

if __name__=='__main__':
    print(fib(4))