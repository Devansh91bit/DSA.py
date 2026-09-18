"""Basic Implementation / creation of Singly Linked list"""
#Creating the class for the nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating the class for the Singly Linked list 
class Singly_Linked_List:
    def __init__(self):
        self.head = None
    