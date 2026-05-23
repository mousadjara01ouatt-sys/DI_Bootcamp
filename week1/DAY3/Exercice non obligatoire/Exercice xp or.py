# Exercice 1 
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def definition(self):
        print("A circle is the set of all points equidistant from a central point.")

circle = Circle(5)
print(f"Perimeter : {circle.perimeter():.2f}")
print(f"Area : {circle.area():.2f}")
circle.definition()


# Exercice 2 
import random

class MyList:
    def __init__(self, letters):
        self.mylist = letters

    def reverse_list(self):
        return self.mylist[::-1]

    def sort_list(self):
        return sorted(self.mylist)

    def random_list(self):
        return [random.randint(1, 100) for _ in self.mylist]

my_list = MyList(['c', 'a', 'b', 'e', 'd'])
print(f"Reversed list : {my_list.reverse_list()}")
print(f"Sorted list : {my_list.sort_list()}")
print(f"Random list : {my_list.random_list()}")


# Exercice 3 
class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        self.menu.append({"name": name, "price": price, "spice": spice, "gluten": gluten})
        print(f"{name} has been added to the menu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"{name} has been updated.")
                return
        print(f"{name} is not on the menu.")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"{name} has been removed from the menu.")
                return
        print(f"{name} is not on the menu.")


manager = MenuManager()
manager.add_item("Pizza", 20, "A", True)
manager.update_item("Soup", 12, "B", False)
manager.remove_item("Salad")



