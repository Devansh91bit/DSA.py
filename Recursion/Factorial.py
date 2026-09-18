x = int(input("Enter the number :\n"))
def factorial(x):
    if x<=1:
        return 1
    return x*factorial(x-1)
print(f"Factorial of {x} = {factorial(x)}")