class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.__price = price
        self.category = category
    def get_price(self):
        
        print(f"The product name is {self.name}, product price is {self.__price}, and their category is{self.category}")
    def set_price(self,new_price):
        self.__price = new_price
        if new_price > 0:
            print(f"The product name is {self.name}, product new price is {self.__price}, and their category is{self.category}")
        else:
            print("Enter positive intiger")
       
phone = Product("Oppo",13999,"Camara_phone")
Phone2 = Product("Vivo",19999,"Gaming_phone")

print(phone.get_price())
print(phone.set_price(12999))
print(Phone2.get_price())
print(Phone2.set_price(18999))