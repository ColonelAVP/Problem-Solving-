# Fn for deletion of a elements in linked list
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

    # fn to search for a node in Linked list
    def search_node(self,node):
        current = self.head
        while current != None:
            if current.data == node:
                return True
            current = current.next
        return False

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
print("\n")
if LL.search_node(31):
    print("Node Found")
else:
    print("Node not found")

