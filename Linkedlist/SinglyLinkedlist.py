"""Basic Implementation / creation of Singly Linked list (Don't expect exceptional handling....)"""
#Creating the class for the nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating the class for the Singly Linked list with operations
class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            else:
                curr.next = new_node
        self.length += 1
        return print("Element added successfully !!")

    def traverse(self):
        if self.length == 0:
            print("Empty linked list, start adding some elements !")
            return
        curr = self.head
        while curr != None:
            print(f"{curr.data} -> ",end="")
            curr = curr.next
        else: print(f"{curr}")
        return

    def pop(self, index = None):
        if self.length == 0:
            print("Empty Linked List, Nothing to pop !!")
            return
        elif index == None:
            curr = self.head
            if curr.next == None:
                self.head = None
            else:
                while curr.next.next != None:
                    curr = curr.next
                else:
                    curr.next = None
        elif index != None:
            curr = self.head
            if index >= self.length:
                print(f"Invalid index passed to pop, the current length of the linked list = {self.length}")
                return
            elif index == 0:
                self.head = curr.next
            else:
                i = 1
                while i < index:
                    curr = curr.next
                    i += 1
                else: 
                   curr.next = curr.next.next
        self.length -= 1    
        print("Element deleted successfully !!")  
        return

    def len(self):
        print(f"The length of the linked list = {self.length}")

    def insert(self, index, data):
        if index == 0:
            new_node = Node(data)
            curr = self.head
            new_node.next = curr
            self.head = new_node
        elif index >= self.length:
            print(f"Invalid index passed to insert, the current length of the linked list = {self.length}")
            return
        else:
            new_node = Node(data)
            curr = self.head
            i = 1
            while i < index:
                curr = curr.next
                i += 1
            else: 
                new_node.next = curr.next
                curr.next = new_node
        self.length += 1
        return print(f"Element inserted successfully at index = {index}")

#Testing linked list and operations through user - Menu driven implementation  
linked_list = Singly_Linked_List()
while True:
    print("\n=======================================================")
    print("1 -> Append an element")
    print("2 -> Insert an element")
    print("3 -> pop an element")
    print("4 -> Print the length of the linked list")
    print("5 -> Print the linked list")
    print("6 -> Exit program \n")
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        x = int(input("Enter the value to append: "))
        linked_list.append(x)
    elif ch == 2:
        index, data = int(input("Enter the index to insert= ")), int(input("Enter the data= "))
        linked_list.insert(index,data)
    elif ch == 3:
        print("Want to pop a certain index element ?")
        print("1 -> Yes / 2 -> No")
        ch2 = int(input("Enter your choice: "))
        if ch2 == 1:
            x = int(input("Enter the index: "))
            linked_list.pop(x)
        elif ch2 == 2:
            linked_list.pop()
        else:
            print("Invalid Input !!")
    elif ch == 4:
        linked_list.len()
    elif ch == 5:
        linked_list.traverse()
    elif ch == 6:
        print("Successfully exited the program ! bye bye !")
        break
    else:
        print("Invalid input !")