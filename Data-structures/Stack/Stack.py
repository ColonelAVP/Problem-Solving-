#creating  a class named stack
class Stack:
    def __init__(self):
        self.stack = []

    # fn adds a item to the stack
    def push(self,item):
        self.stack.append(item)

    # fn removes the last item in stack
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)


list1 = Stack()
list1.push(52)
list1.push(50)
list1.push(51)
print(list1.size())