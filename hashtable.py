class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = []
        for _ in range(size):
            self.table.append([])
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  
    
    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
        print("Key not found!")
    
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

