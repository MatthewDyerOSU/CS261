# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Matthew Dyer

import numpy as np


class DynamicArray:
    
    def __init__(self):
        self.capacity = 10
        self.index = 0
        self.next_index = 0
        self.length = 0
        self.data = np.empty(self.capacity, dtype='O')

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        self.index += 1
        return self.data[self.index]

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= 0:
                if index < self.length:
                    return self.data[index]
                else:
                    raise IndexError
            else:
                raise IndexError
        else:
            raise TypeError

    def __setitem__(self, index, value):
        if isinstance(index, int):
            if index == self.capacity:
                self.data.resize(self.capacity*2)
                self.capacity = self.capacity*2
            self.data[index] = value

    def __delitem__(self, index):
        self[index] = None
        # pass

    # def __contains__(self, item):
    #     pass

    def is_empty(self):
        if self.length == 0:
            return True

    def append(self, value):
        self[self.length] = value
        self.length += 1
        self.next_index += 1

    def clear(self):
        for i in range(self.length):
            del self[i]
        self.length = 0

    def pop(self):
        if self.length == 0:
            raise IndexError
        else:
            last = self[self.length - 1]
            del self[self.length - 1]
            self.length -= 1
            self.next_index -= 1
            return last

    def delete(self, index):
        if self.length == 0:
            raise IndexError
        else:
            if isinstance(index, int):
                if index >= 0: 
                    if index < self.length:
                        del self[index]
                        for i in range(index+1, self.length): 
                            self[i-1] = self[i]
                        self.length -= 1
                        self.next_index -= 1
                        if self.length < self.capacity//2:
                            self.data.resize(self.capacity//2)
                            self.capacity = self.capacity//2
                    else:
                        raise IndexError
                else:
                    raise IndexError
            else:
                raise TypeError

    def insert(self, index, value):
        if isinstance(index, int):
            if index >= 0:
                if index <= self.length:
                    self.length += 1
                    if self.length >= self.capacity:
                        self.data.resize(self.capacity*2)
                        self.capacity = self.capacity*2    
                    self.next_index += 1
                    for i in range(self.length, index, -1):
                        self[i] = self[i-1]
                    self[index] = value
                else:
                    raise IndexError
            else:
                raise IndexError
        else:
            raise TypeError
                    
    def is_full(self):
        if self.length == self.capacity:
            return True
        else:
            return False

    def max(self):
        if self.length > 0:
            maxval = 0
            for i in range(self.length):
                if self[i] > maxval:
                    maxval = self[i]
            return maxval
        else:
            return None        


    def min(self):
        if self.length > 0:
            minval = None
            for i in range(self.length):
                if minval is None or self[i] < minval:
                    minval = self[i]
            return minval
        else:
            return None

    def sum(self):
        if self.length > 0:
            sumval = 0
            for i in range(self.length):
                sumval = sumval + self[i]
            return sumval
        else:
            return None
        
    def linear_search(self, value):
        for i in range(self.length):
            if value == self[i]:
                return i
            
                
    def binary_search(self, value):
        left = 0
        right = self.length - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = self[mid]
            if mid_val == value:
                return mid

            elif value < mid_val:
                right = mid - 1

            else:
                left = mid + 1
        return None
         
    
        
                        

