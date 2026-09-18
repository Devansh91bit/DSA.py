"""Return a list where li[i] represents the rank of the ith element in the given array: """
#taking input
n = int(input("Enter the length of the array !!\n"))
li = [ ]
for i in range(n):
    li.append(int(input("Enter the elements\n")))
print(f"The unsorted array: {li}\n")

#rank of an element in the array
copied = sorted(set(li))
feq_map = dict()
for ind,key in enumerate(copied):
    feq_map[key]=ind
for j in range(n):
    li[j]=feq_map[li[j]]
print(f"The Rank List of the corresponding array (in-place): {li}")