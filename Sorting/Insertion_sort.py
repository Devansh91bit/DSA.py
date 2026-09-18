#Taking input from the user 
n = int(input("Enter the length of the array:\n"))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter the {i}th index Element of the array\n")))
print(f"The array u entered (unsorted)= {arr}\n")

#Implementing Insertion sort to sort the array !
def insertion_sort(arr):
    length = len(arr)
    for i in range(1,length):
        insert_index = i
        curr_element = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > curr_element:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = curr_element
#Printing out the result
insertion_sort(arr)
print(f"Array after sorting: {arr}")