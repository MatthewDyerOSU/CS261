# BinarySearchTree: A binary search tree.
# Matthew Dyer

class BinarySearchTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, new_node):
        new_node.parent = self
        if new_node.key <= self.key:
            if self.left is None:
                self.left = new_node
            else:
                return self.left.insert(new_node)
        else:
            if self.right is None:
                self.right = new_node
            else:
                return self.right.insert(new_node)
        

    def search(self, key):
        if key == self.key:
            return self
        elif key <= self.key:
            if self.left == key:
                return self.left
            elif self.left is None:
                return None
            else:
                return self.left.search(key)
        else:
            if self.right == key:
                return self.right
            elif self.right is None:
                return None
            else:
                return self.right.search(key)

    def delete(self, key):
        if key == self.key:
            if self.is_leaf():
                return self.parent
            elif self.right is not None:
                left_ptr = self.left
                self = self.right
                self.left = left_ptr
            else:
                self = self.left
            self.parent = None
            return self
        elif key <= self.key:
            if self.left is not None:
                if key == self.left.key:
                    deleted_node = self.left
                    self.left = None
                    return deleted_node.parent
        elif key > self.key:
            if self.right is not None:
                if key == self.right.key:
                    deleted_node = self.right
                    self.right = None
                    return deleted_node.parent
        return self

    def is_leaf(self):
        return self.left is None and self.right is None