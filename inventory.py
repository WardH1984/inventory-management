import json

class Inventory:
    def __init__(self, filename="inventory.json"):
        # Initializing an empty dictionary is O(1)
        self.filename = filename
        self.products = {}
        self.load_from_json()

    def add_product(self, name, quantity):
        # Checking if a key exists in a dictionary is O(1) on average
        if name in self.products:
            # Increasing a value for an existing key is also O(1) on average
            self.products[name] += quantity
        else:
            # Adding a new key is O(1) on average, though rare reallocation of the hash table may cost more
            self.products[name] = quantity
        self.save_to_json()
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
            self.save_to_json()
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
        # min() over a dictionary with n elements checks each element once, making this O(n)
        return min(self.products, key=self.products.get)
        # Total time complexity: O(n)

    def save_to_json(self):
        """Saves the inventory to a JSON file."""
        # Writing to a file is O(n) in the number of products
        with open(self.filename, 'w') as file:
            json.dump(self.products, file, indent=4)
        # Total time complexity: O(n)

    def load_from_json(self):
        """Loads the inventory from a JSON file."""
        try:
            # Reading from a file is O(n) in the number of products
            with open(self.filename, 'r') as file:
                self.products = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.products = {}
            self.save_to_json()
        # Total time complexity: O(n)

# Creating an instance of Inventory and loading the JSON file
inv = Inventory()
print(inv.products)