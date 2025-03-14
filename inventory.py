class Inventory:
    def __init__(self):
        # Initializing an empty dictionary is O(1)
        self.products = {}

    def add_product(self, name, quantity):
        # Checking if a key exists in a dictionary is O(1) on average
        if name in self.products:
            # Increasing a value for an existing key is also O(1) on average
            self.products[name] += quantity
        else:
            # Adding a new key is O(1) on average, though rare reallocation of the hash table may cost more
            self.products[name] = quantity
        # Total time complexity: O(1) on average

    def remove_product(self, name, quantity):
        # Checking if the key exists in the dictionary is O(1)
        if name in self.products:
            # Modifying a value for an existing key is O(1)
            self.products[name] -= quantity
            # Checking if the value is <= 0 is O(1)
            if self.products[name] <= 0:
                # Removing a key from the dictionary is O(1) on average
                del self.products[name]
        else:
            # Returning a string is O(1)
            return "Product ain't in inventory"
        # Total time complexity: O(1) on average

    def get_most_frequent_product(self):
        # Checking if the dictionary is empty is O(1)
        if not self.products:
            return None
        # max() over a dictionary with n elements checks each element once, making this O(n)
        return max(self.products, key=self.products.get)
        # Total time complexity: O(n)

    def get_least_frequent_product(self):
        # O(1) check if the dictionary is empty
        if not self.products:
            return None
        
        return min(self.products, key=self.products.get)


inv = Inventory()
inv.add_product("Laptop", 5)
inv.add_product("Mobile", 8)
inv.add_product("Tablet", 3)
inv.add_product("Radio", 5)
inv.remove_product("Radio", 5)
inv.remove_product("Laptop", 2)

print(inv.products)
print(inv.get_most_frequent_product())
print(inv.get_least_frequent_product())
