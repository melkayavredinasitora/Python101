# Create a function for factorial
def factorial(num):
    result = 1
    for k in range(1, num + 1):
        result *= k
    return result
    # Return the factorial of n
def factorialr(num):
    if num == 0:
        return 1
    return factorialr(num-1)*num

# Read input and print result
num = int(input())
f = factorialr(num)
print (f"{num}! = {f}")
