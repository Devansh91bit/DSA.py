"""Given an m x n matrix, return all elements of the matrix in spiral order."""
#taking input
m = int(input("Enter the number of the rows !!\n"))
n = int(input("Enter the number of the columns !!\n"))
li = [[0]*n for i in range(m)]
print(li)
for i in range(m):
    for j in range(n):
        li[i][j] = int(input(f"Enter the element at {i} {j} : \n"))
print(f"The original Matrix : {li}\n")

#Building the spiral traversed result
result = []
top, bottom = 0, n-1
left, right = 0, m-1
while top <= bottom and left <= right:
    for i in range(left, right+1):
        result.append(li[top][i])
    top += 1

    for i in range(top, bottom+1):
        result.append(li[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right,left - 1,-1):
            result.append(li[bottom][i])
        bottom -= 1

    if left <= right:
        for i in range(bottom,top - 1,-1):
            result.append(li[i][left])
        left += 1

print(f"The Array after spiral traversal = {result}")