import random
import string
import matplotlib.pyplot as plt

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

# Assume random_strings is your list of 1,000,000 random strings
hash_table = DLeftHashTable(entries=1000, buckets=1)  # 1000 entries, 1 bucket per entry

# Insert strings into hash table
for string in random_strings:
    hash_table.insert(string, None)

# Count collisions for each index value
collisions1 = [len(bucket) for bucket in hash_table.table]

# Plot collisions for hash function 1
plt.figure(figsize=(10, 6))
plt.bar(range(hash_table.entries * hash_table.buckets), collisions1)
plt.xlabel('Index Value')
plt.ylabel('#Collisions')
plt.title('Collisions for Hash Function 1')
plt.show()

# 4. There a few hot spots in the plot, mainly 4 being high #collisions. The first one is around the 180 index value, another one around the 300 index value.
# The third hot spot is seen near the 375 index value and the last one being neat the 650 index value.  