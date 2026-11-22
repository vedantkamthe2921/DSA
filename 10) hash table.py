#Create a hash table and handle the collisions using linear probing with or without replacement
class HashTable:
    def __init__(self, size, replacement=False):
        self.size = size
        self.table = [None] * size
        self.replacement = replacement
 
    def hash_function(self, key):
        return key % self.size
 
    def insert_without_replacement(self, key):
        index = self.hash_function(key)
 
        for step in range(self.size):
            pos = (index + step) % self.size
 
            if self.table[pos] == key:
                print("Duplicate key:", key)
                return False
 
            if self.table[pos] is None:
                self.table[pos] = key
                return True
 
        print("Hash table is full. Cannot insert", key)
        return False
 
    def insert_with_replacement(self, key):
        home = self.hash_function(key)
 
        if key in self.table:
            print("Duplicate key:", key)
            return False
 
        # If home is empty, insert directly.
        if self.table[home] is None:
            self.table[home] = key
            return True
 
        occupant = self.table[home]
        occupant_home = self.hash_function(occupant)
 
        # Replace only when the occupant is away from its own home.
        if occupant_home != home:
            self.table[home] = key
            displaced = occupant
            start = (home + 1) % self.size
 
            for step in range(self.size - 1):
                pos = (start + step) % self.size
                if self.table[pos] is None:
                    self.table[pos] = displaced
                    return True
 
            # Restore the original table if reinsertion is impossible.
            self.table[home] = occupant
            print("Hash table is full. Cannot insert", key)
            return False
 
        # Occupant is at its own home; use ordinary linear probing.
        for step in range(1, self.size):
            pos = (home + step) % self.size
            if self.table[pos] is None:
                self.table[pos] = key
                return True
 
        print("Hash table is full. Cannot insert", key)
        return False
 
    def insert(self, key):
        if self.replacement:
            return self.insert_with_replacement(key)
        return self.insert_without_replacement(key)
 
    def search(self, key):
        home = self.hash_function(key)
 
        for step in range(self.size):
            pos = (home + step) % self.size
 
            if self.table[pos] is None:
                return -1
 
            if self.table[pos] == key:
                return pos
 
        return -1
 
    def display(self):
        print("\\nIndex\\tKey")
        print("----------------")
        for index, key in enumerate(self.table):
            print(index, "\\t", key if key is not None else "EMPTY")
 
 
def main():
    size = int(input("Enter hash table size: "))
    choice = int(input(
        "Choose collision handling (1: Without replacement, "
        "2: With replacement): "
    ))
 
    if choice not in (1, 2):
        print("Invalid choice.")
        return
 
    ht = HashTable(size, replacement=(choice == 2))
 
    n = int(input("Enter number of keys to insert: "))
    for i in range(n):
        key = int(input("Enter key: "))
        ht.insert(key)
 
    ht.display()
 
    search_key = int(input("\\nEnter key to search: "))
    position = ht.search(search_key)
 
    if position != -1:
        print("Key found at index", position)
    else:
        print("Key not found")
 
 
if __name__ == "__main__":
    main()
