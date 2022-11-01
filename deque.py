# Deque: A deque.
# Your implementation should pass the tests in test_deque.py.
# Matthew Dyer

from llist import dllist

class Deque:
    
    def __init__(self):
        self.items = 0 # tracks number of items in deque
        self.data = dllist() # deque is instantiated as a doubly linked list

    def size(self):
        return self.items # returns number of items in the deque

    def enqueue_left(self, value):
        self.data.appendleft(value) # appends item to the left side of the dllist; O(1)
        self.items += 1 # increments item count

    def enqueue_right(self, value):
        self.data.append(value) # appends item to the right side of the dllist; O(1)
        self.items += 1 # increments item count

    def dequeue_left(self):
        if self.items == 0: # if deque is empty, raises error
            raise ValueError
        else:
            self.items -= 1 # decrements item count
            return self.data.popleft() # returns and removes item from left side of dllist; O(1)
        
    
    def dequeue_right(self):
        if self.items == 0: # if deque is empty, raises error
            raise ValueError
        else:
            self.items -= 1 # decrements item count
            return self.data.pop() # returns and removes item from right side of dllist: O(1)

    def is_empty(self):
        if self.items == 0: # checks if dllist is empty
            return True

    

    