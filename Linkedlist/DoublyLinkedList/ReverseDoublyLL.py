"""Given the head of a doubly linked list, reverse the list and return the head of the reversed doubly linked list."""
#Defining structure class
class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None
        self.prev = None

#Taking user Input
D = int(input("Enter the length of the linked list: \n"))
num = Node()
temp = num
for i in range(D):
    x = int(input(f"Enter the {i}th element of the linked list: \n"))
    temp.next = Node(x)
    temp.next.prev = temp
    temp = temp.next

num = num.next #removing the unnecessary default head
num.prev = None
head = num # the passed parameter for the solution

#Actual Implementation: Simply swap the next and prev pointers, and return the end as it becomes the head of the reversed doubly LL
def reverseDLL(head):
    curr = head
    end = None
    while curr:
        end = curr
        curr.prev, curr.next = curr.next, curr.prev #Swap the pointers
        curr = curr.prev #as the next element is in prev for the reversed DLL
    return end #the head of the reversed DLL

#Providing the output
curr = reverseDLL(head)
while curr:
    print(f"{curr.data}", end = " <--> ")
    curr = curr.next
print(None) 