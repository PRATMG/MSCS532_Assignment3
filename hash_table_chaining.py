"""
This program implements a hash table using chaining for collision resolution. 
A hash table maps keys to values using a hash function that calculates an index for each key.
 In cases where multiple keys map to the same index, we resolve these collisions using linked
lists (chaining). This implementation supports three key operations: insert, search, and delete.
 The hash function uses the modulo operation to distribute the keys uniformly across the slots. 
 By doing so, the hash table efficiently handles collisions, ensuring minimal time complexity for
common operations.
"""

class HashTable:
    def __init__(self, size):
        # Initialize the hash table with empty lists for each slot (for chaining)
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        # Hash function to compute the index based on the key
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert or update a key-value pair
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update if key exists
                return
        self.table[index].append((key, value))  # Append if key doesn't exist

    def search(self, key):
        # Search for a key and return its value, or None if not found
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        # Delete a key-value pair and return True if successful, False otherwise
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the key-value pair
                return True
        return False  # Key not found

    def display(self):
        # Display the hash table contents
        for i, slot in enumerate(self.table):
            print(f"Slot {i}: {slot}")

# Example usage
if __name__ == "__main__":
    ht = HashTable(10)  # Create a hash table with 10 slots

    # Insert key-value pairs
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("grape", 3)
    ht.insert("orange", 4)
    ht.insert("mango", 5)

    # Display the hash table
    print("Hash Table After Insertion:")
    ht.display()

    # Search for keys
    print("\nSearch Results:")
    print(f"Search for 'apple': {ht.search('apple')}")
    print(f"Search for 'banana': {ht.search('banana')}")
    print(f"Search for 'cherry' (not present): {ht.search('cherry')}")

    # Delete a key
    print("\nDeleting 'banana'...")
    ht.delete('banana')

    # Display the hash table after deletion
    print("Hash Table After Deletion:")
    ht.display()
