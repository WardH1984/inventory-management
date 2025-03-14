# inventory-management
A simple inventory management system in Python using Object-Oriented Programming (OOP).


# 🏪 Simple Inventory Management System

This is a basic inventory management system built in Python using Object-Oriented Programming (OOP). It allows adding and removing products from an inventory and retrieving the most and least frequent products.

## 🚀 Features
- Add products with a quantity
- Remove products from inventory
- Get the most frequently stored product
- Get the least frequently stored product

## 🛠️ Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- Dictionary-based data storage

## 📝 Usage Example
```python
inv = Inventory()
inv.add_product("Laptop", 5)
inv.add_product("Mobil", 8)
inv.add_product("Surfplatta", 3)
print(inv.get_most_frequent_product())  # Output: "Mobil"
print(inv.get_least_frequent_product())  # Output: "Surfplatta"
