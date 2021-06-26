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
    def delete_given_node(self,pos):
        if pos == 0:
            cur = self.head
            self.head = cur.next
        else:
            counter = 0
            current = self.head
            while counter < pos-1:
                current = current.next
                counter += 1
            next = current.next.next
            current.next.next = None
            current.next = next
        return self.head


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
LL.delete_given_node(2)
LL.print_llist()

print("\nLinked list after deleting first node")
LL.delete_first()
LL.print_llist()

print("\nLinked list after deleting last node")
LL.delete_last()
LL.print_llist()
