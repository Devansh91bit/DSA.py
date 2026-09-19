"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python."""

#Taking Input
num = int(input("Enter the number: \n"))

#Func to return the Square root of the given number
def sqrt(num):
    low, high = 0, num
    while low <= high:
        mid = (low + high) // 2
        x = mid * mid
        if x == num:
            return mid
        elif x > num:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) // 2
    return abs(mid)

print(f"The square root of {num} = {sqrt(num)} !!")