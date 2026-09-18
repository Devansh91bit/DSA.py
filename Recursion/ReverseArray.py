# Taking input from the user to create the array !
n = int(input("Enter the length of the array :\n"))
arr=[]
for i in range(0,n,1):
    arr.append(int(input(f"Enter the {i}th index input value of array:\n")))
print(f"The array u entered (unsorted) :{arr}\n")

def reverser(arr,low=0,high=len(arr)-1):
    if low>=high:
        return arr
    arr[low],arr[high]=arr[high],arr[low]
    return reverser(arr,low+1,high-1)

print(f"The given Array after Reversing = {reverser(arr)}")