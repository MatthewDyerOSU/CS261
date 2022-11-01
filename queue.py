# Queue
# Matthew Dyer

from llist import sllist

class Queue:
    
    def __init__(self):
        self.items = 0 # tracks number of items in queue
        self.data = sllist() # queue is instantiated as a singly linked list

    def enqueue(self, value):
        self.data.append(value) # appends item to the right (rear) side of the sllist; O(1)
        self.items += 1 # increments item count

    def dequeue(self):
        if self.items == 0: # if queue is empty, raises error
            raise ValueError
        self.items -= 1 # decrements item count
        return self.data.popleft() # returns and removes item from the left (front) side of the sllist; O(1)

    def is_empty(self):
        if self.items == 0: # checks if queue is empty
            return True

    def size(self):
        return self.items # returns item count
