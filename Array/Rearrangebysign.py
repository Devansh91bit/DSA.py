"""Rearrange array by making consecutive +ve and -ve elements sequence but in the same order for the given array consisting equal no of +ve and -ve elements:""" 
#taking input
n = int(input("Enter the length of the array !!\n"))
li = [ ]
for i in range(n):
    li.append(int(input("Enter the elements\n")))
print(f"The unsorted array: {li}\n")

#Re-arranging
result = [0]*n
x, y = 0, 1
for i in range(n):
    if li[i]<0:
        result[y] = li[i]
        y += 2
    else:
        result[x] = li[i]
        x += 2

print(f"The array after re-arranging = {result}")