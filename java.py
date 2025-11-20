import json
import os
class Food:
    def __init__(self, name, food_type ,price):
        self.name = name
        self.food_type = food_type
        self.price = price

    def get_info(self):
        return f"Nomi:{self.name} Turi:{self.food_type} Narxi:{self.price}"

    def to_dict(self):
        return {
            "name": self.name,
            "food_type": self.food_type,
            "price": self.price
        }

class Restaurant:
    def __init__(self, name, json_file = "menu.json"):
        self.name = name
        self.json_file = json_file
        self.foods = []

        self.load_json()

    def load_json(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as file:
                data = json.load(file)
                for item in data:
                    food = Food(item["name"], item["food_type"], item["price"])
                    self.foods.append(food)

    def save_json(self):
        data = [food.to_dict() for food in self.foods]
        with open(self.json_file, "w") as new_info:
            json.dump(data, new_info, indent=4)

    def add_food(self, new_food):
        if new_food not in self.foods:
            self.foods.append(new_food)
            self.save_json()

    def delete_food(self, deleted_food):
        for i in self.foods:
            if i.name == deleted_food:
                self.foods.remove(deleted_food)
                self.save_json()

    def update_food(self, old_name, new_name = None, new_type = None, new_price = None):
        for i in self.foods:
            if i.name == old_name:
                if new_name:
                    i.name = new_name
                if new_type:
                    i.food_type = new_type
                if new_price:
                    i.price = new_price
                self.save_json()
                return True
            return False
    def show_all_foods(self):
        for i in self.foods:
            print(i.get_info())
p1 = Restaurant("Milliy Taomlar")
s1 = Food("osh", "ovqat", 30000)
s2 = Food("Manti", "ovqat", 28000)
s3 = Food("Sho`rva", "ovqat", 20000)

p1.add_food(s1)
p1.add_food(s2)
p1.add_food(s3)
p1.show_all_foods()