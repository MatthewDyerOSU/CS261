# AVLTree: A Self-balancing Binary Search Tree
# Matthew Dyer

class AVLTree:
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.key = key
        self.parent = None
        self.balance_factor = 0

    #Add additional methods as needed. Use the helper methods provided below.
                
    def _calculate_balance_factor(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node._is_left_child():
                node.parent.balance_factor += 1
            elif node._is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self._calculate_balance_factor(node.parent)

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                self.rotate_right(node.right)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                self.rotate_left(node.left)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def rotate_left(self, old_root):
        new_root = old_root.right
        old_root.right = new_root.left
        if new_root._has_left_child():
            new_root.left.parent = old_root
        new_root.parent = old_root.parent
        if not old_root._is_root_node():
            if old_root._is_left_child():
                old_root.parent.left = new_root
            else:
                old_root.parent.right = new_root
        new_root.left = old_root
        old_root.parent = new_root
        old_root.balance_factor = old_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(old_root.balance_factor, 0)

    def rotate_right(self, old_root):
        new_root = old_root.left
        old_root.left = new_root.right
        if new_root._has_right_child():
            new_root.right.parent = old_root
        new_root.parent = old_root.parent
        if not old_root._is_root_node():
            if old_root._is_right_child():
                old_root.parent.right = new_root
            else:
                old_root.parent.left = new_root
        new_root.right = old_root
        old_root.parent = new_root
        old_root.balance_factor = old_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(old_root.balance_factor, 0)
    
    def _root_node(self):
        if self._is_root_node():
            return self
        else:
            return self.parent._root_node()  

    # You will need to modify this method
    def insert(self, node):
        if node.key <= self.key:
            if not self._has_left_child():
                self.left = node
                node.parent = self 
                self._calculate_balance_factor(self.left)
            else:
                self.left.insert(node)
        else:
            if not self._has_right_child():
                self.right = node
                node.parent = self
                self._calculate_balance_factor(self.right)
            else:
                self.right.insert(node)
        return self._root_node()
    
    # Do not modify these helper functions. They are included for your convenience,
    def _is_left_child(self):
        return self.parent.left is self

    def _is_right_child(self):
        return self.parent.right is self

    def _is_root_node(self):
        return self.parent is None
 
    def _is_leaf(self):
        return not (self.has_left_child() or self.has_right_child())

    def _has_left_child(self):
        return not self.left is None

    def _has_right_child(self):
        return not self.right is None

    def _has_left_child_only(self):
        return not self.left is None and self.right is None

    def _has_right_child_only(self):
        return not self.right is None and self.left is None