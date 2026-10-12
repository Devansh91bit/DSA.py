"""Given the head of a doubly Linked List and a key x . Delete all occurrences of the given key x if it is present and return the new DLL.
Example: 
Input: 2<->2<->10<->8<->4<->2<->5<->2, x = 2
Output:  10<->8<->4<->5
Explanation: 
All Occurrences of 2 have been deleted.

Constraints:
1 ≤ size of linked list ≤ 105
0 ≤ node.data ≤ 109"""
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
target = int(input("Enter the value to be deleted from the DLL : "))
num = num.next #removing the unnecessary default head
num.prev = None
head = num # the passed parameters for the solution
x = target

#Actual Implementation:Manage the prev and next pointers as we traverse through the DLL
def deleteOccurences(head, x):
    while head: #checks for the head itself, in case empty DLL or no other element at all
        if head.data == x:
            head = head.next
        else: break
    if head == None:
        return None
    head.prev = None

    end, temp = head, head.next if head.next else None #Two pointer approach: one checks the value, one connects the final DLL
    while temp:
        if temp.data == x: #simply move to next node in case the current value has to be deleted
            temp = temp.next
            continue
        else: #connect the end pointer with the current temp node for the required DLL
            end.next = temp
            temp.prev = end
        end = end.next # update the pointers
        temp = temp.next
    end.next = None #Disconnects the resultant DLL with the further deleted Nodes

    return head

#Providing the output
curr = deleteOccurences(head,x)
while curr:
    print(f"{curr.data}", end = " <--> ")
    curr = curr.next
print(None)