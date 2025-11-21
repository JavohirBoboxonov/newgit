class Product:
    def __init__(self, name, product_type, price, year):
        self.name = name
        self.product_type = product_type
        self.price = price
        self.year = year

    def get_info(self):
        return f"Name: {self.name}\nProduct Type: {self.product_type}\nPrice: {self.price}\nYear: {self.year}"


class ElectronicProduct(Product):
    def __init__(self, name, product_type, price, year, battery):
        super().__init__(name, product_type, price, year)
        self.battery = battery
        self.electricity = []

    def add_electronic_product(self, new_product):
        if new_product not in self.electricity:
            self.electricity.append(new_product)

    def remove_product(self, removed_product):
        if removed_product in self.electricity:
            self.electricity.remove(removed_product)
            print(f"{removed_product} Mahsuloti o'chirildi")
        else:
            print("Mahsulot topilmadi")

    def get_info(self):
        return f"""
    Name:{self.name}
    Product Type:{self.product_type}
    Price:{self.price}
    Year:{self.year}
    Battery:{self.battery}
    """


class FurnitureProduct(Product):
    def __init__(self, name, product_type, price, year, quality):
        super().__init__(name, product_type, price, year)
        self.quality = quality
        self.furnitures = []

    def add_furniture_product(self, new_product):
        if new_product not in self.furnitures:
            self.furnitures.append(new_product)

    def remove_product(self, removed_product):
        if removed_product in self.furnitures:
            self.furnitures.remove(removed_product)
            print(f"{removed_product} Mahsuloti o'chirildi")
        else:
            print("Mahsulot topilmadi")

    def get_info(self):
        return f"""
    Name:{self.name}
    Product Type:{self.product_type}
    Price:{self.price}
    Year:{self.year}
    Quality:{self.quality}
    """


class Food(Product):
    def __init__(self, name, product_type, price, limit, year):
        super().__init__(name, product_type, price, year)
        self.limit = limit
        self.foods = []

    def add_food_product(self, new_product):
        if new_product not in self.foods:
            self.foods.append(new_product)

    def remove_product(self, removed_product):
        if removed_product in self.foods:
            self.foods.remove(removed_product)
            print(f"{removed_product} Mahsuloti o'chirildi")
        else:
            print("Mahsulot topilmadi")

    def get_info(self):
        return f"""
    Name:{self.name}
    Product Type:{self.product_type}
    Price:{self.price}
    Year:{self.year}
    Limit:{self.limit}
    """


class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            print(f"{product.name} mahsuloti {self.name} do'koniga qo'shildi")
        else:
            print(f"{product.name} mahsuloti allaqachon mavjud!")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} mahsuloti {self.name} do'konidan o'chirildi")
        else:
            print(f"{product.name} mahsuloti do'konda topilmadi!")

    def list_products(self):
        if self.products:
            print(f"\n{self.name} do'konidagi mahsulotlar:")
            for product in self.products:
                print(product.get_info())
        else:
            print(f"{self.name} do'konida mahsulotlar yo'q!")
shop = Shop("Shop")


electronic1 = ElectronicProduct("Smartphone", "Electronics", 500, 2023, 4000)
furniture1 = FurnitureProduct("Sofa", "Furniture", 300, 2022, "High")
food1 = Food("Pizza", "Food", 15, "2023-11-01", 2025)

shop.add_product(electronic1)
shop.add_product(furniture1)
shop.add_product(food1)