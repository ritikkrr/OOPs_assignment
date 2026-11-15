class Product:
    def __init__(self,device_name,price):
        self.device_name = device_name
        self.price = price
    def status(self):
        print(f"The device name is {self.device_name} and its price is {self.price}")

class Electronic_product(Product):
    def __init__(self, device_name, price,Warranty_year):
        super().__init__(device_name, price)
        self.warranty_year = Warranty_year
    def get_info(self):
        return(f"The device name is {self.device_name}, it's price is {self.price}, and it's warranty is {self.warranty_year} year")
Phone = Electronic_product("sumsumg",21999,2)
print(Phone.get_info())