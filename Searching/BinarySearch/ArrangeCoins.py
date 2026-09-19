"""You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build."""

#Taking input
num = int(input("Enter the number of coins: \n"))

#Func to find out the number of complete rows of coins:
def coinrows(num):
    low , high = 1, num + 1
    while low <= high:
        mid = (low + high) // 2
        x = mid*((mid + 1) / 2 )
        if x == num:
            return mid
        elif x > num:
            if (mid - 1)*(mid / 2) > num:
                high = mid - 1
            else:
                return mid - 1
        else:
            if (mid + 1)*((mid + 2) / 2) < num:
                low = mid + 1
            else:
                return mid 
    return mid

print(f"The number of complete rows formed with {num} coins = {coinrows(num)} !!")