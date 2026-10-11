"""Basic Implementation / creation of Doubly Linked list (Don't expect exceptional handling....)"""
#Creating the class for the nodes
class Node: 
    def __init__(self, data = 0, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

#Creating the class for actual LinkedList operations and Implementations
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.end = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None: 
            self.head = new_node
            self.end = new_node
            self.length += 1
        else:
            self.end.next = new_node
            new_node.prev = self.end
            self.end = new_node
            self.length += 1
        return print("Element added successfully !!")

    def insert(self, index, data):
        if index < 0 or index > self.length:
            return print("Invalid Index passed to insert !!")
        else:
            new_node = Node(data)
            if index == 0 and self.length == 0:
                self.head = new_node
                self.end = new_node
            elif index == 0 and self.length > 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif index == self.length:
                self.end.next = new_node
                new_node.prev = self.end
                self.end = new_node
            else:
                i, curr = 1, self.head
                while i < index:
                    curr = curr.next
                    i += 1
                curr.next.prev = new_node
                new_node.next = curr.next
                curr.next = new_node
                new_node.prev = curr
            self.length += 1
            return print(f"Elemented inserted successfully at index = {index} !!")

    def pop(self, index = None):
        if self.head == None:
            return print("No element to delete !! Linked List is already Empty !!")
        else:
            poped_val = None
            if index == None:
                if self.length == 1:
                    poped_val = self.head.data
                    self.head = None
                    self.end = None
                else:
                    poped_val = self.end.data
                    self.end = self.end.prev
                    self.end.next = None
            else:
                if index == 0 and self.length == 1:
                    poped_val = self.head.data
                    self.head = None
                    self.end = None
                elif index == 0  and self.length > 1:
                    poped_val = self.head.data
                    self.head = self.head.next
                    self.head.prev = None
                elif index > 0 and index < self.length:
                    i, curr = 1, self.head
                    while i < index:
                        i += 1
                        curr = curr.next
                    poped_val = curr.next.data
                    if curr.next.next:
                        curr.next = curr.next.next
                        curr.next.prev = curr
                    else:
                        curr.next = None
                        self.end = curr
                else:
                    print("Invalid Index passed to pop !!")
                    return poped_val
        self.length -= 1
        print("Element popped Successfully !!")
        return poped_val

    def __len__(self):
        return self.length

    def traverse(self):
        if self.length == 0:
            return print("Empty Linked List !! Add some Elements first !!")
        elif self.length == 1:
            return print(f"{self.head.data} -> {None}")
        else:
            i, curr = 0, self.head
            while i < self.length:
                print(f"{curr.data}", end = " <--> ")
                curr = curr.next
                i += 1
            print(None)
        return 

#Testing linked list and operations through user - Menu driven implementation  
linked_list = DoublyLinkedList()
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
            y = linked_list.pop(x)
            print(f"Poped value = {y}")
        elif ch2 == 2:
            y = linked_list.pop()
            print(f"Poped value = {y}")
        else:
            print("Invalid Input !!")
    elif ch == 4:
        print(f"The length of the Linked List = {len(linked_list)}")
    elif ch == 5:
        linked_list.traverse()
    elif ch == 6:
        print("Successfully exited the program ! bye bye !")
        break
    else:
        print("Invalid input !")