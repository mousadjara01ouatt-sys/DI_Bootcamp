#Exercice 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Felix", 5)
cat2 = Cat("Luna", 9)
cat3 = Cat("Milo", 3)

def find_oldest_cat(cat1, cat2, cat3):
    return max([cat1, cat2, cat3], key=lambda cat: cat.age)

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")


#Exercice 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 30)

print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the bigger dog.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is the bigger dog.")
else:
    print("Both dogs are the same size.")


#Exercice 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's 
                 Obuying a stairway to heaven"])
stairway.sing_me_a_song()


#Exercice 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.grouped_animals = {}

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)
        self.grouped_animals = self.sort_animals()

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        self.grouped_animals = self.sort_animals()

    def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals:
            letter = animal[0]
            if letter not in groups:
                groups[letter] = []
            groups[letter].append(animal)
        return groups

    def get_groups(self):
        for letter, animals in self.grouped_animals.items():
            print(f"{letter}: {animals}")


brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cat", "Cougar", "Lion", "Zebra")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()