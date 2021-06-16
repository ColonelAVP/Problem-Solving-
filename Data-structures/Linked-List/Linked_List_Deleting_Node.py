# Fn for deletion of given node in linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_llist(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data,end="->")
                temp = temp.next

    def insert_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # fn to delete first node in a linked list
    def delete_first(self):
        self.head = self.head.next

    # fn to delete last node in a linked list
    def delete_last(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    # fn to delete a given node
    def delete_at_given_pos(self,key):
        temp = self.head
        while temp.next.data != key:
            temp = temp.next
        next = temp.next.next
        temp.next = next


# Driver's Code
LL = LinkedList()
LL.insert_start(10)
LL.insert_start(20)
LL.insert_start(30)
LL.insert_start(40)
LL.insert_start(50)
LL.insert_start(60)

print("Actual Linked List")
LL.print_llist()

print("\nLinked List after Deleting a given node")
LL.delete_at_given_pos(40)
LL.print_llist()

print("\nLinked list after deleting first node")
LL.delete_first()
LL.print_llist()

print("\nLinked list after deleting last node")
LL.delete_last()
LL.print_llist()