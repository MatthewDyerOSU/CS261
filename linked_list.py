# LinkedList: A doubly-linked list.
# Has an insert_in_order that, when used, keeps the values of
# each node in ascending order.
# Matthew Dyer

class LinkedList:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value 
        if next == None:
            self.next = self
        else:
            self.next = next
        if prev == None:
            self.prev = self
        else:
            self.prev = prev
    
    def is_sentinel(self):
        if self.value == None:
            return True
        else:
            return False

    def is_empty(self):
        if self.next == self and self.prev == self:
            return True
        else:
            return False

    def is_last(self):
        if self.is_empty():
            if self.is_sentinel():
                return True
            else:
                return False
        else:
            if self.is_sentinel():
                return False
            else:
                return True

    def last(self):
        if self.is_empty():
            if self.is_sentinel():
                return self
            else:
                return None
        else:
            return self.prev

    def append(self, new_node):
        if self.is_empty():
            self.next = new_node
            self.prev = new_node
            new_node.prev = self
            new_node.next = self
        else:
            prev_ptr = self.prev
            self.prev = new_node
            prev_ptr.next = new_node
            new_node.prev = prev_ptr
            new_node.next = self

    def delete(self):
        next_ptr = self.next
        prev_ptr = self.prev
        del self
        prev_ptr.next = next_ptr
        next_ptr.prev = prev_ptr

    def insert(self, new_node):
        next_ptr = self.next
        next_ptr.prev = new_node
        new_node.prev = self
        new_node.next = next_ptr
        self.next = new_node

    def at(self, index):
        ctr = 0
        node = self
        while ctr != index:
            node = node.next
            ctr += 1
        return node

    def search(self, value):
        self.value = value
        node = self.next
        while node.value != value:
            node = node.next
        self.value = None
        if node.is_sentinel():
            return None
        return node

    def insert_in_order(self, new_node):
        if self.is_empty():
            self.append(new_node)
        else:
            node = self.next
            while new_node.value < node.value:
                node = node.next
            node.insert(new_node)

    def __repr__(self):
        node_list = []
        node = self.next
        while not node.is_sentinel():
            node_list.append(str(node.value))
            node = node.next
        return " -> ".join(node_list)