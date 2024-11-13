
import getpass

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class UserManager:
    def __init__(self):
        self.users = {
            "admin": User("admin", "admin123", "Admin"),
            "user1": User("user1", "user123", "User")
        }

    def authenticate_user(self, username, password):
        password = password.strip()
        print(f"Debug: Entered password for {username} is '{password}'")
        
        if username in self.users and self.users[username].password == password:
            return self.users[username]
        else:
            return None

    def prompt_login(self):
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        user = self.authenticate_user(username, password)
        return user


class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price}, Stock: {self.stock_quantity}"


class Inventory:
    def __init__(self):
        self.products = []
        self.low_stock_threshold = 5

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added successfully!")

    def delete_product(self, product_id):
        product = self.find_product(product_id)
        if product:
            self.products.remove(product)
            print(f"Product '{product.name}' deleted successfully!")
        else:
            print("Product not found!")

    def update_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        product = self.find_product(product_id)
        if product:
            if name:
                product.name = name
            if category:
                product.category = category
            if price is not None:
                product.price = price
            if stock_quantity is not None:
                product.stock_quantity = stock_quantity
            print(f"Product '{product.name}' updated successfully!")
        else:
            print("Product not found!")

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def view_all_products(self):
        if not self.products:
            print("No products available in the inventory.")
        else:
            for product in self.products:
                print(product)

    def search_by_name(self, name):
        found = [product for product in self.products if name.lower() in product.name.lower()]
        if found:
            for product in found:
                print(product)
        else:
            print("No products found with that name.")

    def filter_by_category(self, category):
        found = [product for product in self.products if category.lower() in product.category.lower()]
        if found:
            for product in found:
                print(product)
        else:
            print("No products found in that category.")

    def check_stock_levels(self):
        for product in self.products:
            if product.stock_quantity <= self.low_stock_threshold:
                print(f"Warning: Product '{product.name}' is low on stock! ({product.stock_quantity})")

def main():
    user_manager = UserManager()
    inventory = Inventory()

    print("Welcome to the Inventory Management System")

    user = None
    while user is None:
        user = user_manager.prompt_login()
        if user is None:
            print("Invalid credentials. Please try again.")
        else:
            print(f"Welcome {user.username} ({user.role})")

    while True:
        print("\nMenu:")
        print("1. View all products")
        print("2. Search products by name")
        print("3. Filter products by category")
        print("4. Check stock levels")
        
        if user.role == "Admin":
            print("5. Add new product")
            print("6. Update existing product")
            print("7. Delete product")
        
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.view_all_products()

        elif choice == "2":
            name = input("Enter product name to search: ")
            inventory.search_by_name(name)

        elif choice == "3":
            category = input("Enter category to filter by: ")
            inventory.filter_by_category(category)

        elif choice == "4":
            inventory.check_stock_levels()

        elif choice == "5" and user.role == "Admin":
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            stock_quantity = int(input("Enter product stock quantity: "))
            product = Product(len(inventory.products) + 1, name, category, price, stock_quantity)
            inventory.add_product(product)

        elif choice == "6" and user.role == "Admin":
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name (leave empty to keep current): ")
            category = input("Enter new product category (leave empty to keep current): ")
            price = input("Enter new product price (leave empty to keep current): ")
            stock_quantity = input("Enter new stock quantity (leave empty to keep current): ")

            price = float(price) if price else None
            stock_quantity = int(stock_quantity) if stock_quantity else None

            inventory.update_product(product_id, name, category, price, stock_quantity)

        elif choice == "7" and user.role == "Admin":
            product_id = int(input("Enter product ID to delete: "))
            inventory.delete_product(product_id)

        elif choice == "0":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()



