"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

#Defining structure class
class LinkedNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

#Taking user input
D1 = int(input("Enter the number of digits of first number:\n"))
num1 = LinkedNode()
curr = num1
for _ in range(D1):
    x = int(input("Enter the Digits in reversed order of num1:\n"))
    curr.next = LinkedNode(x)
    curr = curr.next

D2 = int(input("Enter the number of digits of Second number:\n"))
num2 = LinkedNode()
curr = num2
for _ in range(D2):
    x = int(input("Enter the Digits in reversed order of num2:\n"))
    curr.next = LinkedNode(x)
    curr = curr.next

num1, num2 = num1.next, num2.next # Removing the unnecessary default head
head1, head2 = num1, num2 # The heads provided for the solution so that the actual linked list numbers don't get lost
# Actual Implementation: Adding these 2 reversed numbers as linked list (assuming head1, head2 is passed as parameters)
result = LinkedNode()
temp = result
carry = 0
while head1 or head2 or carry:
    val1 = head1.data if head1 else 0
    val2 = head2.data if head2 else 0
    add = val1 + val2 + carry
    carry = add // 10
    add = add % 10
    temp.next = LinkedNode(add)
    temp = temp.next
    head1 = head1.next if head1 else None
    head2 = head2.next if head2 else None

#Providing the Output
temp = result.next
while temp:
    print(temp.data, end = " -> ")
    temp = temp.next
print(None)