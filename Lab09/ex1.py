class DLeftHashTable:
    def DLeftHashTable(self, entries, buckets):
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