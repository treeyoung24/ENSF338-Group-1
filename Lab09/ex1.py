class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.entries = entries
        self.buckets = buckets
        self.table = [[] for _ in range(entries * buckets)]

    def _hash_function(self, key):
        return hash(key) % (self.entries * self.buckets)

    def insert(self, key, value):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def lookup(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None


# Example usage:
hash_table = DLeftHashTable(entries=5, buckets=3)
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)

print(hash_table.lookup("apple"))  # Output: 10
print(hash_table.lookup("banana"))  # Output: 20
print(hash_table.lookup("orange"))  # Output: 30
print(hash_table.lookup("grape"))  # Output: None
