""" func to return the length of longest subarray of a given array int nums, with int K. The subarray can't contain any element with more occurance than k """
# Taking input from the user
n = int(input("Enter the number of elements:\n"))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter the {i}th element\n")))
print(f"The entered array : {arr}\n")
K = int(input("Enter the K (Atmost - number of occurances of an element)\n"))

def maxlength (arr,K):
    n = len(arr)
    longest = 0
    left = 0
    hash_map = dict()
    for right in range(n):
        hash_map[arr[right]] = hash_map.get(arr[right],0) + 1
        while hash_map[arr[right]] > K:
            hash_map[arr[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)
    return longest

#Using the func
print(f"The longest length of such a possible sub-array = {maxlength(arr,K)}\n")