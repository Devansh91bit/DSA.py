# Taking input from the user to create the array !
n = int(input("Enter the length of the array :\n"))
arr=[]
for i in range(0,n,1):
    arr.append(int(input(f"Enter the {i}th index input value of array:\n")))
print(f"The array u entered (unsorted) :{arr}\n")

# Implementing Bubble sort for sorting the array !
def bubble_sort(arr):
    # use local length so function works for any array
    length = len(arr)
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            # swap if out of order (ascending)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
                break

# Sort and print the result
bubble_sort(arr)
print(f"The array after sorting :{arr}")