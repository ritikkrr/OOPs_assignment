class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"product ({self.name}, {self.price},{self.category})"
    def __add__(self, other):
        return self.price + other.price

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
    def remove_product(self,name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                break

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    def show_all_products(self):
        for product in self.products:
            print(product)

class Store:
    def __init__(self,store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        ## take input from user side
        name = input("Enter the product name")
        price = float(input("Enter the product price name"))
        category = input("Enter product name:")
        new_product = Product(name, price, category)
        self.inventory.add_product(new_product)
        print(f"{name} added successfully!\n")

    def show_summary(self):
        total_item = len(self.inventory.products)
        total_value = self.inventory.get_total_value()
        print(f"Total Items:{total_item}")
        print(f"Total Value {total_value}")

my_store = Store("Tech Gadgets")
p1 = Product("laptop",29999,"Electric")
p2 = Product("Mouse",299,"Electric")



my_store.inventory.add_product(p1)
my_store.inventory.add_product(p2)

my_store.show_summary()

print("\n All product in Inventory:")
my_store.inventory.show_all_products()

combine = p1+p2
print(f"\n combine price of {p1.name} and {p2.name}:{combine}")

    
        