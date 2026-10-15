"""Given a sorted array arr[], find the transition point, i.e., the first index where K element was observed. If arr does not have any K element, return -1."""

#taking input
n = int(input("Enter the length of the array !!\n"))
li = [ ]
for i in range(n):
    li.append(int(input("Enter the elements\n")))
print(f"The entered sorted array: {li}\n")

k = int(input("Enter the element to be search for the first index: "))

#Actual Implementation: Func to find the first occurence of any element in the given array
def transitionPoint(arr, k): 
        # Code here
        n = len(arr)
        i, j = 0, n-1
        ind = n
        while i <= j:
            mid = (i + j) // 2
            if arr[mid] == k:
                ind = min(ind, mid)
                j = mid - 1
            elif arr[mid] < k:
                i = mid + 1
            else:
                j = mid - 1  
        if ind == n: return -1
        else:
            return ind

#Print the output
print(f"The first index where the {k} element occur in the given array = {transitionPoint(li,k)} !!")
