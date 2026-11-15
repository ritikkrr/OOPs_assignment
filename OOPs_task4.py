class Product:
    def get_info (self):
        return "this will return about product"

class Laptop(Product):
    def __init__(self,name,price,processor):
        
        self.name = name
        self.price = price
        self.processor = processor
    def get_info(self):
        return f"The name of laptop is {self.name}, it's price {self.price} and it's processor is {self.processor}"

class Mobile(Product):
    def __init__(self,name,price,processor):
        
        self.name = name
        self.price = price
        self.processor = processor
    def get_info(self):
        return f"The name of Mobile is {self.name}, it's price {self.price} and it's processor is {self.processor}"
prod = Product()
laptop_1  = Laptop("Rahul","hello","occ")
mobile_1  = Mobile("Oppo","10999","octacore")

products = [laptop_1,mobile_1]
for product in products:
    print(product.get_info())