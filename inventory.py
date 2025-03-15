import json
import os

def clear():
    os.system('cls')

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

def main():
    inventory = Inventory()

    while True:
        clear()
        print("\n--Inventory Menu---")
        print("1. Check inventory")
        print("2. Add product")
        print("3. Remove product")
        print("4. Show most frequent product")
        print("5. Show least frequent product")
        print("6. End program")

        choice = input("> ")

        if choice == "1":
            clear()
            print("Inventory balance:")
            if inventory.products:
                for product, quantity in inventory.products.items():
                    print(f"{product}: {quantity}")
            else:
                print("Inventory is empty.")

            input("\nPress [Enter] to continue...")

        elif choice == "2":
            name = input("Enter a product: ")
            try:
                quantity = int(input("Enter quantity: "))
                inventory.add_product(name, quantity)
                print(f"{quantity} of {name} have been added to inventory.")
            except ValueError:
                print("Enter a number not float.")

            input("\nPress [Enter] to continue...")

        elif choice == "3":
            name = input("Enter a product: ")
            try:
                quantity = int(input("Enter quantity: "))
                inventory.remove_product(name, quantity)
                print(f"{quantity} have been removed from {name}.")
            except ValueError:
                print("Enter a number not float.")

            input("\nPress [Enter] to continue...")

        elif choice == "4":
             product = inventory.get_most_frequent_product()
             if product:
                 print(f"Most frequent item is: {product}, {inventory.products[product]} in inventory.")

             input("\nPress [Enter] to continue...")

        elif choice == "5":
            product = inventory.get_least_frequent_product()
            if product:
                print(f"Less frequent item is {product}, {inventory.products[product]} is in inventory.")
            else:
                print("Inventory is empty.")

            input("\nPress [Enter] to continue...")

        elif choice == "6":
            print("Ending the program.")
            break


if __name__ == "__main__":
    main()