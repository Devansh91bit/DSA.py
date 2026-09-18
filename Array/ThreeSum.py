"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""

#taking input
n = int(input("Enter the length of the array !!\n"))
li = [ ]
for i in range(n):
    li.append(int(input("Enter the elements\n")))
print(f"The original array: {li}\n")

#Finding the triplets
li.sort()
result = set()
for i in range(n-1):
    left, right = i + 1, n - 1
    while left < right:
        if li[i] + li[left] + li[right] == 0:
            result.add((li[i],li[left],li[right]))
            left += 1
        elif li[i] + li[left] + li[right] > 0:
            right -= 1
        else:
            left += 1
result = [list(x) for x in result]
print(f"The unique triplets pairs are= {result}")