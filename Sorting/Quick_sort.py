# Taking input from the user
n = int(input("Enter the length of the array !\n"))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter the {i}th Index Element ! \n")))
print(f"The array u entered (unsorted)= {arr}\n")

#Function to fix array and return pivot index
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

#Function to perform recursion and check base condition
def quick_sort(arr,low=0,high=None):
    if high ==None:
        high = len(arr)-1
    if low < high:
        pivot_index = partition(arr,low,high)
        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1,high)

quick_sort(arr)
print(f"The array after Quick sort: {arr}")
