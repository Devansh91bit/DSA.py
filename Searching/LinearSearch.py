"""This is the simplest thing one can ever face..."""
#taking input
n = int(input("Enter the length of the array !!\n"))
li = [ ]
for i in range(n):
    li.append(int(input("Enter the elements\n")))
print(f"The Original array: {li}\n")
target = int(input("Enter the Element you want to search : \n"))

#Linear Search xD
def linear_search(arr, target, exists = False):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return True, i
    else: return False, -1

exists, index = linear_search(li, target)
print(f"The target exists = {exists} in the given array at index {index}")