import sys

class Supplier:
    def __init__(self, supplier_id, supplier_name):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name

    def display_supplier(self):
        print(f"Supplier ID: {self.supplier_id}, Name: {self.supplier_name}")


class Product:
    def __init__(self, product_id, product_name, price, supplier, weight, color):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.supplier = supplier
        self.spec = self.Specification(weight, color)

    # Inner class
    class Specification:
        def __init__(self, weight, color):
            self.weight = weight
            self.color = color

        def display_spec(self):
            print(f"Weight: {self.weight}, Color: {self.color}")

    def display_product(self):
        print(f"\nProduct ID: {self.product_id}")
        print(f"Name: {self.product_name}")
        print(f"Price: {self.price}")

        print("Specifications:")
        self.spec.display_spec()

        print("Supplier Details:")
        self.supplier.display_supplier()


# ---------------- MAIN PROGRAM ----------------

products = []
suppliers = []

while True:
    print("\n1. Add Supplier")
    print("2. Add Product")
    print("3. Display Products")
    print("4. Show Reference Count")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        sid = int(input("Enter Supplier ID: "))
        sname = input("Enter Supplier Name: ")

        sup = Supplier(sid, sname)
        suppliers.append(sup)

        print("Supplier added.")
        print("Reference count of supplier:", sys.getrefcount(sup))

    elif choice == 2:
        if not suppliers:
            print("No suppliers available! Add supplier first.")
            continue

        pid = int(input("Enter Product ID: "))
        pname = input("Enter Product Name: ")
        price = float(input("Enter Price: "))

        print("Available Suppliers:")
        for sup in suppliers:
            print(f"{sup.supplier_id} - {sup.supplier_name}")

        sid = int(input("Enter Supplier ID: "))
        selected_supplier = None

        for sup in suppliers:
            if sup.supplier_id == sid:
                selected_supplier = sup
                break

        if not selected_supplier:
            print("Invalid Supplier!")
            continue

        weight = input("Enter Weight: ")
        color = input("Enter Color: ")

        prod = Product(pid, pname, price, selected_supplier, weight, color)
        products.append(prod)

        print("Product added.")
        print("Reference count of product:", sys.getrefcount(prod))
        print("Reference count of supplier (after linking):", sys.getrefcount(selected_supplier))

    elif choice == 3:
        if not products:
            print("No products available.")
        else:
            for prod in products:
                prod.display_product()

    elif choice == 4:
        print("\n--- Reference Count Details ---")
        for prod in products:
            print(f"Product {prod.product_name}:", sys.getrefcount(prod))
        for sup in suppliers:
            print(f"Supplier {sup.supplier_name}:", sys.getrefcount(sup))

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")