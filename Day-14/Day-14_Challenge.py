#- Calculate factorial recursively
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Example usage
print("Factorial of 5 is:", factorial(5))  # Output: 120
