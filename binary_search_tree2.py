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
         if not self.has_left_child():
               self.left = new_node
         else:
               return self.left.insert(new_node)
      else:
         if not self.has_right_child():
               self.right = new_node
         else:
               return self.right.insert(new_node)
      

   def search(self, key):
      if key == self.key:
         return self
      elif key <= self.key:
         if self.left == key:
               return self.left
         elif not self.has_left_child():
               return None
         else:
               return self.left.search(key)
      else:
         if self.right == key:
               return self.right
         elif not self.has_right_child():
               return None
         else:
               return self.right.search(key)

   def delete(self, node_to_delete):
      if node_to_delete != self.key:
         if not self.is_leaf():
            if node_to_delete > self.key:
               return self.right.delete(node_to_delete)
            else: # node_to_delete < self.key
               return self.left.delete(node_to_delete)
         else: # no children/no match
            return self.root()
      else: # found a match
         if self.is_leaf():
            if self.parent is None:
               return self.parent
            else:
               if self.parent.left == self:
                  self.parent.left = None
               else:
                  self.parent.right = None
         elif self.has_one_child():
            if self.has_left_child():
               self.left.parent = self.parent
               if self.parent is not None:
                  if self.parent.left == self:
                     self.parent.left = self.left
                  else:
                     self.parent.right = self.left
               self = self.left
            else: # has_right_child():
               self.right.parent = self.parent
               if self.parent is not None:
                  if self.parent.left == self:
                     self.parent.left = self.right
                  else:
                     self.parent.right = self.right
               self = self.right
         else: # has 2 children
            replacement = self.right.minimum()
            self.delete(self.right.minimum().key)
            replacement.parent = self.parent
            replacement.left = self.left
            replacement.right = self.right
            if self.parent is not None:
               if self.parent.left == self:
                  self.parent.left = replacement
               else:
                  self.parent.right = replacement
            self = replacement
         return self.root()
         
   
   def is_leaf(self):
      return not self.has_left_child() and not self.has_right_child()

   def has_left_child(self):
      return self.left is not None

   def has_right_child(self):
      return self.right is not None

   def has_one_child(self):
      return (self.right is None and self.left is not None) or (self.right is not None and self.left is None)


   def minimum(self):
      if self.has_left_child():
         return self.left.minimum()
      return self

   def root(self):
      if self.parent is None:
         return self
      else:
         return self.parent.root()
      
   def keys(self, order):
      if order == 'pre':
         return self.preorder()
      elif order == 'in':
         return self.inorder()
      elif order == 'post':
         return self.postorder()
      else:
         print("Incorrect Input, must be 'pre', 'in', or 'post'")

   def preorder(self):
      key_list = []
      key_list.append(self.key)
      if not self.is_leaf():
         key_list = key_list + self.left.preorder()
         key_list = key_list + self.right.preorder()
      return key_list

   def inorder(self):
      key_list = []
      if not self.is_leaf():
         key_list = key_list + self.left.inorder()
      key_list.append(self.key)
      if not self.is_leaf():
         key_list = key_list + self.right.inorder()
      return key_list

   def postorder(self):
      key_list = []
      if not self.is_leaf():
         key_list = key_list + self.left.postorder()
         key_list = key_list + self.right.postorder()
      key_list.append(self.key)
      return key_list



        