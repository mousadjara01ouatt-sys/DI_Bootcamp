class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, **kwargs):
        for animal_type, count in kwargs.items():
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

    def get_info(self):
        result = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            result += f"{animal} : {count}\n"
        result += "\n    E-I-E-I-0!"
        return result

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = self.get_animal_types()
        named = []

        # Liste des pluriels irreguliers
        irregular_plurals = {
            "sheep": "sheep",
            "deer": "deer",
            "fish": "fish"
        }

        for animal in animal_list:
            if self.animals[animal] > 1:
                if animal in irregular_plurals:
                    named.append(irregular_plurals[animal])
                else:
                    named.append(f"{animal}s")
            else:
                named.append(animal)

        # On ajoute "and" avant le dernier animal
        if len(named) > 1:
            result = ", ".join(named[:-1]) + f" and {named[-1]}"
        else:
            result = named[0]

        return f"The {self.name}'s farm has {result}."


macdonald = Farm("McDonald")
macdonald.add_animal(cow=5, sheep=2, goat=12)
print(macdonald.get_info())
print(macdonald.get_short_info())