import os

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_price(self):
        return self.price * self.quantity

class Receipt:
    TAX_RATE = 0.08
    DISCOUNT_RATE = 0.05  # For example, 5% discount on total

    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def calculate_subtotal(self):
        return sum(item.total_price() for item in self.items)
    
    def calculate_tax(self):
        return self.calculate_subtotal() * self.TAX_RATE
    
    def calculate_discount(self):
        return self.calculate_subtotal() * self.DISCOUNT_RATE
    
    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        discount = self.calculate_discount()
        return subtotal + tax - discount
    
    def generate_receipt(self):
        lines = []
        lines.append("Receipt")
        lines.append("=" * 30)
        
        for item in self.items:
            lines.append(f"{item.name:20} Rs.{item.price:.2f} x {item.quantity} = Rs.{item.total_price():.2f}")
        
        lines.append("=" * 30)
        lines.append(f"Subtotal:     Rs.{self.calculate_subtotal():.2f}")
        lines.append(f"Tax (8%):     Rs.{self.calculate_tax():.2f}")
        lines.append(f"Discount (5%):-Rs.{self.calculate_discount():.2f}")
        lines.append("=" * 30)
        lines.append(f"Total:        Rs.{self.calculate_total():.2f}")
        
        return "\n".join(lines)
    
    def save_receipt(self, filename):
        receipt_text = self.generate_receipt()
        with open(filename, 'w') as file:
            file.write(receipt_text)
        print(f"Receipt saved to {filename}")

def main():
    receipt = Receipt()
    
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input(f"Enter price for {name}: Rs."))
        quantity = int(input(f"Enter quantity for {name}: "))
        
        item = Item(name, price, quantity)
        receipt.add_item(item)
    
    print("\nReceipt Preview:\n")
    print(receipt.generate_receipt())
    
    filename = input("Enter filename to save receipt (e.g., receipt.txt): ")
    receipt.save_receipt(filename)

if __name__ == "__main__":
    main()
