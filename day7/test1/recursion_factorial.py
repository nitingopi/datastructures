def factorial(value) -> int:
    return 1 if value == 0 else value * factorial(value-1)

print(factorial(5))    
