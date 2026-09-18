# Taking input from the user to create the array !
n = int(input("Enter the length of the array :\n"))
arr=[]
for i in range(0,n,1):
    arr.append(int(input(f"Enter the {i}th index input value of array:\n")))
print(f"The array u entered (unsorted) :{arr}\n")

#Implementing Selection sort to sort the array !
def selection_sort(arr):
    length = len(arr)
    for i in range(length-1):
        min_ind = i
        for j in range(i+1,length):
            if arr[j]<arr[min_ind]:
                min_ind = j
        arr[i],arr[min_ind] = arr[min_ind],arr[i]

# Sort and print the result
selection_sort(arr)
print(f"The array after sorting: {arr}\n") 
