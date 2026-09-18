"""Return the given array with all unique elements in the front in place"""
n = int(input("Enter the length of the array !!\n"))
li = [ ]
for i in range(n):
    li.append(int(input("Enter the elements\n")))
print(f"The unsorted array: {li}\n")

def shift_dup(arr):
    hash_map = dict()
    for i in arr:
        hash_map[i]=0
    #python3.7+ have dict = ordered
    j = 0
    for i in hash_map:
        arr[j]=i
        j+=1
    return j # Number of unique elements pushed in front of array

print(f"The no of unique elements in the array: {shift_dup(li)}")
print(f"The array after shifting duplicates : {li}")
