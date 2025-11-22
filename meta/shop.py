class Product:
    def __init__(self, name, price, year, product_type):
        self.name = name
        self.price = price
        self.year = year
        self.product_type = product_type

    def get_info(self):
        return f"""
        Name:{self.name}
        Price: {self.price}
        Year: {self.year}
        Product Type: {self.product_type}
    """

class ElectronicProduct(Product):
    def __init__(self, name, price, year, product_type, battery):
        super().__init__(name, price, year, product_type)
        self.battery = battery
        self.electronic_products = []

    def add_electronic_products(self, new_product):
        if new_product not in self.electronic_products:
            self.electronic_products.append(new_product)

    def remove_electronic_products(self, removed_product):
        if removed_product in self.electronic_products:
            self.electronic_products.remove(removed_product)
        else:
            print("Afsuski Bu Mahsulot Topilmadi")
    def info_all_products(self):
        for i in self.electronic_products:
            print(i.get_info())

    def get_info(self):
        return f"""
Name:{self.name}
Price:{self.price}
Year:{self.year}
Product:{self.product_type}
Battery:{self.battery}
"""

class Furniture(Product):
    def __init__(self, name, price, year, product_type, quality):
        super().__init__(name, price, year, product_type)
        self.quality = quality
        self.furniture_products = []

    def add_furniture_products(self, new_products):
        if new_products not in self.furniture_products:
            self.furniture_products.append(new_products)

    def remove_products(self, removed_products):
        if removed_products in self.furniture_products:
            self.furniture_products.remove(removed_products)
        else:
            print("Bunday Mahsulot Topilmadi")

    def get_info(self):
        return f"""
Name:{self.name}
Price:{self.price}
Product Type:{self.product_type}
Year:{self.year}
Sifati:{self.quality}
"""

class Os(Product):
    def __init__(self, name, price, year, product_type, version):
        super().__init__(name, price, year, product_type)
        self.version = version
        self.operation_systems = []

    def add_operating_system(self, new_system):
        if new_system not in self.operation_systems:
            self.operation_systems.append(new_system)

    def remove_system(self, removed_system):
        if removed_system in self.operation_systems:
            self.operation_systems.remove(removed_system)
        else:
            print("Bunday Os Topilmadi")

    def get_info(self):
        return f"""
Name: {self.name}
Price: {self.price}
Product Type: {self.product_type}
Year: {self.year}
System:{self.version}
"""

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        if new_product not in self.products:
            self.products.append(new_product)

    def remove_products(self, removed_products):
        if removed_products in self.products:
            self.products.remove(removed_products)

    def update_product_info(self, product_name, **kwargs):
        for product in self.products:
            if product.name == product_name:
                for key, value in kwargs.items():
                    if hasattr(product, key):
                        setattr(product, key, value)
                    else:
                        print(f"{key} - {product_name} mahsulotida bunday atribut yo'q.")
                print(f"{product_name} mahsuloti muvaffaqiyatli yangilandi.")
                return
        print(f"{product_name} nomli mahsulot topilmadi.")
    def get_systems(self):
        for i in self.products:
            if i.product_type == "os":
                print(f"Os Turidagi Mahsulotlar {i.get_info()}")

    def get_furniture(self):
        for i in self.products:
            if i.product_type == "furniture":
                print(f"Mebel Turidagi Mahsulotlar {i.get_info()}")
    def get_electronic(self):
        for i in self.products:
            if i.product_type == "electron":
                print(f"ELectron Qurilmalar {i.get_info()}")

    def get_info(self):
        for i in self.products:
            print(i.get_info())
d1 = Shop("Pepsi Market")

s1 = Os("Windows", "10$ for month", 2021, "os", "11")
s2 = Furniture("Shkaf", 400000, 2025, "furniture", "A`lo")
s3 = ElectronicProduct("Hp noutbook", 5000000, 2023, "electron", "4000 mA")
d1.add_product(s1)
d1.add_product(s2)
d1.add_product(s3)
print(d1.get_systems())
print(d1.get_electronic())
print(d1.get_furniture())