# MaxHeap: A binary 'max' heap.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_max_heap.py.
# Matthew Dyer

class MaxHeap:
    
    def __init__(self):
        self._data = []

    def _size(self):
        return len(self._data)

    def __len__(self):
        return self._size()

    def _is_empty(self):
        return self._size() == 0

    def _last_index(self):
        return self._size() - 1

    def _value_at(self, index):
        if index < 0 or index >= self._size():
            raise IndexError
        return self._data[index]

    def _left_child_index(self, parent_index):
        return (2*parent_index)+1

    def _right_child_index(self, parent_index):
        return (2*parent_index)+2

    def _parent_index(self, child_index):
        return (child_index-1)//2

    def _parent(self, child_index):
        parent = self._value_at(self._parent_index(child_index))
        if isinstance(parent, int):
            if self._parent_index(child_index) > self._size():
                raise IndexError
        return parent

    def _left_child(self, parent_index):
        if self._left_child_index(parent_index) >= self._size():
            return None
        else:
            return self._value_at(self._left_child_index(parent_index))

    def _right_child(self, parent_index):
        if self._right_child_index(parent_index) >= self._size():
            return None
        else:
            return self._value_at(self._right_child_index(parent_index))

    def _has_left_child(self, parent_index):
        return self._left_child_index(parent_index) < self._size()

    def _has_right_child(self, parent_index):
        return self._right_child_index(parent_index) < self._size()

    def _greater_child_index(self, parent_index):
        if self._has_left_child(parent_index) or self._has_right_child(parent_index):
            if not self._has_right_child(parent_index):
                return self._left_child_index(parent_index)
            elif self._left_child(parent_index) >= self._right_child(parent_index):
                return self._left_child_index(parent_index)
            else:
                return self._right_child_index(parent_index)
        else:
            return None

    def _obeys_heap_property_at_index(self, index):
        if self._has_left_child(index) or self._has_right_child(index):
            if isinstance(self._left_child(index), int):
                if self._value_at(index) < self._left_child(index):
                    return False
            if isinstance(self._right_child(index), int):
                if self._value_at(index) < self._right_child(index):
                    return False
        return True

    def _swap(self, index0, index1):
        stored_value = self._value_at(index0)
        self._data[index0] = self._value_at(index1)
        self._data[index1] = stored_value

    def _sift_down(self, index):
        if not self._obeys_heap_property_at_index(index):
            next_index = self._greater_child_index(index)
            self._swap(index, self._greater_child_index(index))
            self._sift_down(next_index)

    def _sift_up(self, index):
        if self._parent_index(index) >= 0:
            if self._value_at(index) > self._parent(index):
                next_index = self._parent_index(index)
                self._swap(index, self._parent_index(index))
                self._sift_up(next_index)

    def insert(self, value):
        self._data.append(value)
        self._sift_up(self._last_index())

    def delete(self):
        if self._is_empty():
            return None
        else: 
            self._swap(0, self._last_index())
            deleted = self._data.pop()
            self._sift_down(0)
            return deleted