# creating a class named Queue
class Queue:
    def __init__(self):
        self.queue = []

    # fn adds a item to the queue
    def enqueue(self,item):
        self.queue.append(item)

     # fn removes the first item from Queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

list2 = Queue()
list2.enqueue(20)
list2.enqueue(15)
print(list2.size())
list2.dequeue()
print(list2.size())