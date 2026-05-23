class Pets():
    def __init__(self, animals):
        """Initialise la liste des animaux de compagnie."""
        self.animals = animals

    def walk(self):
        """Fait marcher tous les animaux."""
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        """Initialise un chat avec un nom et un âge."""
        self.name = name
        self.age = age

    def walk(self):
        """Retourne une description de la marche du chat."""
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        """Fait chanter le Bengal."""
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        """Fait chanter le Chartreux."""
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        """Fait chanter le Siamois."""
        return f'{sounds}'


bengal_obj = Bengal('Leo', 3)
chartreux_obj = Chartreux('Luna', 5)
siamese_obj = Siamese('Milo', 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)
sara_pets.walk()