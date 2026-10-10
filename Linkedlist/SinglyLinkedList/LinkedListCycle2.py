"""Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list."""

#Defining structure class
class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

#Taking user Input
n = int(input("Enter the number of elements in the Linked List: "))
cycled = int(input("Enter the index where the cycle begins (-1 if don't want to add any cycle):"))
LL = ListNode()
curr = LL
end = None
for i in range(n):
    z = int(input(f"Enter the element at {i}th index: "))
    temp = ListNode(z)
    curr.next = temp
    curr = curr.next
    end = curr

if cycled == -1: pass #i.e the input linked list contains no cycle 
elif cycled >= 0 and cycled < n: #checks in case invalid - index passed for cycle
    i, curr = 0, LL.next
    while i != cycled:
        i += 1
        curr = curr.next
    end.next = curr #Sets the cycle

LL = LL.next #removing the unnecessary default head
head = LL # the passed parameter for the solution

#Actual Implementation: Floyd Cycle method 
def CycleStart(head):
    slow, fast = head, head
    cycle_exists, index = False, -1
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_exists = True
            slow, index = head, 0 #Sets the slow pointer back to the head + index is initialized to 0 as cycle confirmed
            while slow != fast:
                index += 1
                slow = slow.next
                fast = fast.next
            return cycle_exists, slow, index
    return cycle_exists, None, index # Returns False, None as cycle doesn't exists with -1 index as expected.

#Providing the Output
cycle, begins_at, index = CycleStart(head)
print(f"Cycle exists in the given Linked list = {cycle}, begins at = {begins_at} with index = {index} !!")