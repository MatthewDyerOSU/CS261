# PriorityQueue: An efficient priority queue.
# Matthew Dyer

from max_heap import MaxHeap

class PriorityQueue:
    
    def __init__(self):
        self.heap = MaxHeap()

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        return self.heap.delete()

    def is_empty(self):
        return len(self.heap) == 0