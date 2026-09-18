import sys
print("Enter the number: \n")
n = int(sys.stdin.readline())
def fibonacci(x):
    if x<=1:
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)
print(f"Fibonacci of {n} = {fibonacci(n)}")