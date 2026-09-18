""" Func to return the indices of two elements in an array whose sum is equal to the Target, Return -1 if no such two indices exist in the given array"""
# Taking input from the user
n = int(input("Enter the number of elements:\n"))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter the {i}th element\n")))
print(f"The entered array : {arr}\n")
target = int(input("Enter the Target: \n"))

def twosum(arr,target):
    hash_map = dict()
    n = len(arr)
    for i in range(n): #We can also use enumerate here...
        remaining = target - arr[i]
        if remaining in hash_map:
            return hash_map[remaining],i
        hash_map[arr[i]] = i 
    else:
        return -1

#Using the func
print(f"The indices of the elements : {twosum(arr,target)}\n")