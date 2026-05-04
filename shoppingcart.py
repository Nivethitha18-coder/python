# Base Class
class Product:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.price = 0

    def getDetails(self):
        self.id = input("Enter Product ID: ")
        self.name = input("Enter Product Name: ")
        self.price = float(input("Enter Price: "))

    def add_to_cart(self, cart):
        cart.append(self)
        print(f"{self.name} added to cart.")

    def display(self):
        print("\n--- Product Details ---")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Price:", self.price)


# Derived Class - Electronics
class Electronics(Product):
    def __init__(self):
        super().__init__()
        self.name_of_product = ""
        self.brand = ""
        self.warranty = ""

    def getElectronicsDetails(self):
        self.name_of_product = input("Enter Electronics Product Name: ")
        self.brand = input("Enter Brand: ")
        self.warranty = input("Enter Warranty: ")

    def display(self):   # Polymorphism
        super().display()
        print("--- Electronics Details ---")
        print("Product:", self.name_of_product)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)


# Derived Class - Clothing
class Clothing(Product):
    def __init__(self):
        super().__init__()
        self.type = ""
        self.size = ""
        self.color = ""

    def getClothDetails(self):
        self.type = input("Enter Clothing Type: ")
        self.size = input("Enter Size: ")
        self.color = input("Enter Color: ")

    def display(self):   # Polymorphism
        super().display()
        print("--- Clothing Details ---")
        print("Type:", self.type)
        print("Size:", self.size)
        print("Color:", self.color)


# -------- Main Program --------
cart = []
n = int(input("Enter number of products to add: "))

for i in range(n):
    print(f"\n--- Enter details for Product {i+1} ---")
    print("Choose product type:")
    print("1. Electronics")
    print("2. Clothing")

    choice = int(input("Enter choice (1-2): "))

    if choice == 1:
        e = Electronics()
        e.getDetails()
        e.getElectronicsDetails()
        e.add_to_cart(cart)

    elif choice == 2:
        c = Clothing()
        c.getDetails()
        c.getClothDetails()
        c.add_to_cart(cart)

    else:
        print("Invalid choice! Skipping this product.")

# Display Cart
print("\n===== Shopping Cart Items =====")
subtotal = 0
for item in cart:
    item.display()
    subtotal += item.price

# Billing
discount = 0.1 * subtotal   # 10% discount
tax = 0.05 * (subtotal - discount)  # 5% tax after discount
grand_total = subtotal - discount + tax

print("\n===== BILL SUMMARY =====")
print("Subtotal:", subtotal)
print("Discount (10%):", discount)
print("Tax (5%):", tax)
print("Grand Total:", grand_total)