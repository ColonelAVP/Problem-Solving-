# fn to detect loop and remove using Floyd-Marshal Algorithm
# Time Complexity = O(n) & Space Complexity = O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    # fn to print the List
    def print_linked_list(self):
        temp = self.head
        while (temp):
            print(temp.data, end="->")
            temp = temp.next

    # fn to add a node at the beginning of list
    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def detectloopFMA(self):
        slow = self.head
        fast = self.head
        while slow.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow.data == fast.data:
                slow.next = None
                break
        return

# Driver's Code
LL1 = Linkedlist()
LL1.insert_start(6)
LL1.insert_start(5)
LL1.insert_start(4)
LL1.insert_start(3)
LL1.insert_start(2)
LL1.insert_start(1)
LL1.head.next.next.next.next.next.next = LL1.head.next
#LL1.print_linked_list()
LL1.detectloopFMA()
LL1.print_linked_list()


