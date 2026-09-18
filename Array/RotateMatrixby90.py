"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation."""

#taking input
n = int(input("Enter the number of the rows/columns !!\n"))
li = [[0]*n for i in range(n)]
print(li)
for i in range(n):
    for j in range(n):
        li[i][j] = int(input(f"Enter the element at {i} {j} : \n"))
print(f"The unrotated Matrix : {li}\n")

#Rotating (90 = transpose + reverse row, 180 = reverse row + reverse column, 270 = transpose + reverse col)
for i in range(n):
    for j in range(0,i):
        li[i][j] , li[j][i] = li[j][i], li[i][j]

for i in range(n):
    left, right = 0, n-1
    while left < right:
        li[i][left], li[i][right] = li[i][right], li[i][left]
        left, right = left + 1, right - 1

print(f"The Matrix after 90 degree rotation = {li}")