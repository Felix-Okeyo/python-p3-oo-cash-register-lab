#!/usr/bin/env python3

# Define a class called CashRegister to manage transactions and calculate totals
class CashRegister:
    # Constructor method (gets called when creating a new CashRegister instance)
    def __init__(self, discount=0):
        # Initialize starting values
        self.total = 0  # Keeps track of the total cost of items
        self.transactions = []  # Stores information about each transaction
        self.discount = discount  # Holds the discount percentage
        self.items = []  # Keeps track of the items bought
        
    # Method to add items to the register
    def add_item(self, title, price, quantity=1):
        item_total = quantity * price
        self.total += item_total  # Update the total cost
        self.transactions.append({"title": title, "price": price})  # Store transaction info
        self.items.extend([title] * quantity)  # Keep track of items
        
    # Method to calculate the current total
    def calculate_total(self):
        return self.total  # Return the total cost of all items
    
    # Method to apply a discount to the total
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)  # Calculate discount amount
            self.total -= discount_amount  # Reduce the total cost after discount
            print(f"After the discount, the total comes to {self.total:.2f}")  # Print updated total
        else:
            print("There is no discount to apply.")  # Print if no discount is available
        
    # Method to get details of the last transaction
    def get_last_transaction(self):
        if self.transactions:
            return self.transactions[-1]  # Return information about the last transaction
        return None  # Return None if there are no transactions
        
    # Method to void (cancel) the last transaction
    def void_last_transaction(self):
        if self.transactions:
            last_transaction = self.transactions.pop()  # Remove the last transaction
            self.total -= last_transaction["price"]  # Reduce total cost accordingly
            self.items.remove(last_transaction["title"])  # Remove the item from the list of items bought


# Create a CashRegister instance with a discount (optional)
register = CashRegister(discount=10)

# Add items to the register
register.add_item("Item 1", 10.00, quantity=2)
register.add_item("Item 2", 20.00)

# Calculate and print the total before applying a discount
print("Total before discount:", register.calculate_total())

# Apply discount (if applicable) and print updated total
register.apply_discount()

# Get and print details of the last transaction
last_transaction = register.get_last_transaction()
print("Last Transaction:", last_transaction)

# Void the last transaction and calculate the total again
register.void_last_transaction()
print("Total after voiding last transaction:", register.calculate_total())
