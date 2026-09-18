"""Return all elements from the given array with frequencies >1 """
#Get an Input array 
n = int(input("Enter the length of the array :\n"))
arr=[]
for i in range(0,n,1):
    arr.append(int(input(f"Enter the {i}th index input value of array:\n")))
print(f"The array u entered (unsorted) :{arr}\n")

#Hashing -> Pre storing info into some data structure (here to count frequencies)
hash_map = dict()
for i in arr:
    hash_map[i] = hash_map.get(i,0)+1
print(hash_map)
#makes it easier to work on that data (filtering keys with >1 frequencies)
multiples = [x for x in hash_map if hash_map[x]>1]
print(multiples)
