"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place."""

#taking input
m = int(input("Enter the number of the rows !!\n"))
n = int(input("Enter the number of the columns !!\n"))
li = [[0]*n for i in range(m)]
print(li)
for i in range(m):
    for j in range(n):
        li[i][j] = int(input(f"Enter the element at {i} {j} : \n"))
print(f"The original Matrix : {li}\n")

#setting zeros in-place
rows = [0]*m
columns = [0]*n
for i in range(m):
    for j in range(n):
        if li[i][j] == 0:
            rows[i], columns[j] = 1, 1

for i in range(m):
    for j in range(n):
        if rows[i] or columns[j] == 1:
            li[i][j] = 0

print(f"The matrix after Setting zeros = {li}")