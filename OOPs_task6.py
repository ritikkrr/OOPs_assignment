class Product:
    def __init__(self,name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"product name=(self.name),price={self.price},category = {self.category}"

    def __add__(self, other):
        return self.price +other.price

product_1 = Product("laptop",24999,"processor")
product_2= Product("Mouse",299,"wire")
print(product_1+product_2)

    