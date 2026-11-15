class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        if self.price >= 15000: ## i want the phone price is above or equal to 15000 then i will discount 8%
            ab = self.price - self.price*8/100
            print(f"The product name is {self.name}, product price is {ab}, and their category is{self.category} ")
        else:
        
            print(f"The product name is {self.name}, product price is {self.price}, and their category is{self.category}")

phone = Product("Oppo",13999,"Camara_phone")
Phone2 = Product("Vivo",19999,"Gaming_phone")

print(phone.get_info())
print(Phone2.get_info())
        