"""Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity."""

#Defining structure class
class LinkedNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

#Taking user Input
D = int(input("Enter the length of the linked list: \n"))
num = LinkedNode()
temp = num
for i in range(D):
    x = int(input(f"Enter the {i}th element of the linked list: \n"))
    temp.next = LinkedNode(x)
    temp = temp.next

num = num.next #removing the unnecessary default head
head = num # the passed parameter for the solution

#Actual Implementation: Grouping Odd nodes first (by index) followed by Even indexed nodes
def OddEvenLinkedList(head):
    if not head: #To check edge-case: Empty Linked list
        return None
    curr = head
    even = LinkedNode()
    temp = even
    end = None
    while curr:
        if curr.next:
            holder = curr.next
            curr.next = curr.next.next
            curr = curr.next
            holder.next = None
            temp.next = holder
            temp = temp.next
            continue
        end = curr
        curr = curr.next

    end.next = even.next
    return head

#Providing the Output
curr = OddEvenLinkedList(head)
while curr:
    print(curr.data, end = " -> ")
    curr = curr.next
print(None)