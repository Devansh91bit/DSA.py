"""Given the head of a linked list, remove the nth node from the end of the list and return its head."""

#Defining structure class
class LinkedNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

#Taking user input
D = int(input("Enter the length of the linked list: \n"))
num1 = LinkedNode()
curr = num1
for i in range(D):
    x = int(input(f"Enter the element at the {i}th index:\n"))
    curr.next = LinkedNode(x)
    curr = curr.next
num1 = num1.next #removing the unnecessary default head
head = num1 #the passed parameter for the solution
n = int(input("Enter the position from the end to remove the element: \n"))

#Actual implementation: remove the nth node from the end of the linked list
def removefromend(head,n):
    curr = head
    if not curr:
        return None
    length = 0 #calculating length because it will help later
    while curr:
        length += 1
        curr = curr.next
    #using length to know the nth position from the front of LL (from head)
    curr, n = head, length - n #set curr back to head + n from front of LL
    if n < 0: return None #edge case if n is out of LL length
    elif n == 0: #edge case if the first node is to be removed (head itself)
        head = head.next
        return head
    i = 1
    while i < n: #this will set our curr pointer right before the node required to be removed
        i += 1
        curr = curr.next
    curr.next = curr.next.next if curr.next.next else None #skip the next node (hence removed it)
    return head

#Providing the Output
curr = removefromend(head, n)
while curr:
    print(curr.data, end = " -> ")
    curr = curr.next
print(None)
