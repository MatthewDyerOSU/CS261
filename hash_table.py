# Hashtable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Matthew Dyer


class HashTable:
    
    def __init__(self, size=20):
        self.size = size # set size equal to value provided, if none provided size is 20
        self.data = [ [] for _ in range(self.size) ] # create a list of empty lists equal to size
        
    def __setitem__(self, key, value):
        index = self.hash(key) # creates index location no larger than size
        if len(self.data[index]) != 0: # checks if anything to iterate over
            for i in self.data[index]: # iterates over KVP's(lists) at index
                if i[0] == key:
                    del i[1]
                    i.append(value) # if key already exists, replace value
                else: 
                    self.data[index].append([key, value]) # else add new KVP
        else:
            self.data[index].append([key, value]) # else add new KVP
            

    def __getitem__(self, key):
        index = self.hash(key) # creates index location no larger than size
        for i in self.data[index]: # iterates over KVP's(lists) at index
            if i[0] == key: 
                return i[1] # if key is found, return value

    def hash(self, key):
        return hash(key) % self.size # Will provide an index no larger than size

    def delete(self, key):
        index = self.hash(key) # creates index location no larger than size
        if len(self.data[index]) != 0: # check if anything to iterate over
            for i in self.data[index]: # iterates over KVP's(lists) at index
                if i[0] == key:
                    i[1] = None # if the key exists, set value to None

    def clear(self):
        del self.data # deletes the entire data structure(list)
        self.data = [ [] for _ in range(self.size) ] # creates a new list of empty lists

    def keys(self):
        keys = [] # empty list for storing keys
        if self.size != 0: # check if anything to iterate over
            for i in self.data: # iterates over index locations
                if len(i) != 0: # check if index location has anything to iterate over
                    for j in i: # iterates over KVP's
                        keys.append(j[0]) # adds the key to list
        return keys

    def values(self):
        values = [] # empty list for storing values
        if self.size != 0: # check if anything to iterate over
            for i in self.data: # iterates over index locations
                if len(i) != 0: # check if index location has anything to iterate over
                    for j in i: # iterates over KVP's
                        values.append(j[1]) # adds the value to list
        return values
        

