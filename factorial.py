def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Test the function
number = int(input("Enter a non-negative integer to find its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", number, "is", factorial(number))
