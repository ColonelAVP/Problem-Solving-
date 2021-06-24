# Fn to print a Binary tree (Inorder)(Iterative)

class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

def print_Inorder(root):
    current = root
    stack = []
    while True:
        if current!= None:
            stack.append(current)
            current = current.left
        elif stack:
            key = stack.pop()
            print(key.val,end="->")
            current = key.right
        else:
            break
    return

# Driver's Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print_Inorder(root)










