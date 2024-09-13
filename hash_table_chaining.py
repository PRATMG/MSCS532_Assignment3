
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    # Simple hash function using modulo
    def hash_function(self, key):
        return hash(key) % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    # Search for value associated with a key
    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    # Delete key-value pair
    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

# Test block to check the functionality of the HashTable class
if __name__ == "__main__":
    # Create a hash table with 10 slots
    ht = HashTable(10)

    # Insert some key-value pairs
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("grape", 30)

    # Print hash table state after insertions
    print("Hash Table after insertions:")
    print(ht.table)

    # Search for a key
    print("\nSearch for 'apple':", ht.search("apple"))
    print("Search for 'banana':", ht.search("banana"))
    print("Search for 'orange' (not present):", ht.search("orange"))

    # Delete a key
    print("\nDelete 'banana':", ht.delete("banana"))
    print("Delete 'orange' (not present):", ht.delete("orange"))

    # Print hash table state after deletions
    print("\nHash Table after deletions:")
    print(ht.table)
