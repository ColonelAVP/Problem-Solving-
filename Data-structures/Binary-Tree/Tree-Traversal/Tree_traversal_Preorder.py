# fn to print a binary tree (Preorder)

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

# Iterative
def print_Preorder(root):
    current = root
    stack = []
    stack.append(current)
    while stack:
        val = stack.pop()
        print(val.data,end="->")
        if val.right:
            stack.append(val.right)
        if val.left:
            stack.append(val.left)
    return

# Driver's Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print_Preorder(root)