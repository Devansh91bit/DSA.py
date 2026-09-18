# Taking input from the user to create the array !
n = int(input("Enter the length of the array :\n"))
arr=[]
for i in range(0,n,1):
    arr.append(int(input(f"Enter the {i}th index input value of array:\n")))
print(f"The array u entered (unsorted) :{arr}\n")

#Function to merge the sorted arrays !!
def merge_array(left,right):
    n,m = len(left),len(right)
    result = []
    i,j=0,0
    while i<n and j<m :
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    else:
        while j<m:
            result.append(right[j])
            j+=1
    return result

#Function to divide the array and perform recursion !!
def merge_sort(li):
    n = len(li)
    if n==1:
        return li
    x = n//2
    left_half = li[:x:]
    right_half = li[x::]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge_array(left_half,right_half)

# Sort and print the result
print(f"The array after sorting :{merge_sort(arr)}")