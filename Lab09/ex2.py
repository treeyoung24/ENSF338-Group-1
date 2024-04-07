import random
import string

def generate_random_string():
    length = random.randint(1, 10)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

random_strings = [generate_random_string() for _ in range(1000000)]

class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.entries = entries
        self.buckets = buckets
        self.table = [[] for _ in range(entries * buckets)]

    def _hash_function1(self, key):
        return hash(key) % (self.entries * self.buckets)

    def _hash_function2(self, key):
        return (hash(key) * 2 + 1) % (self.entries * self.buckets)

    def insert(self, key, value):
        index1 = self._hash_function1(key)
        index2 = self._hash_function2(key)
        for item in self.table[index1]:
            if item[0] == key:
                item[1] = value
                return
        for item in self.table[index2]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index1].append([key, value])

    def lookup(self, key):
        index1 = self._hash_function1(key)
        index2 = self._hash_function2(key)
        for item in self.table[index1]:
            if item[0] == key:
                return item[1]
        for item in self.table[index2]:
            if item[0] == key:
                return item[1]
        return None