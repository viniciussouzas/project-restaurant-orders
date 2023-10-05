import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = set()
        self.load_menu()
    
    def load_menu(self):
        data = self.read_file(self.path)

        for line in data[1:]:
            dish_name, price_str, ingredient_name, amount_str = line

            price = float(price_str)

            ingredient = Ingredient(ingredient_name)

            amount = int(amount_str)

            dish = Dish(dish_name, price)

            if dish in self.dishes:
                for d in self.dishes:
                    if d == dish:
                        d.add_ingredient_dependency(ingredient, amount)
            else:
                dish.add_ingredient_dependency(ingredient, amount)
                self.dishes.add(dish)
                        
                        
    
    def read_file(self, path):
        with open(path, encoding="utf-8") as file:
            file = csv.reader(file, delimiter=",", quotechar='"')
            return list(file)

