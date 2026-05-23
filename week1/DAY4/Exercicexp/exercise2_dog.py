class Dog:
    def __init__(self, name, age, weight):
        """Initialise un chien avec un nom, un âge et un poids."""
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        """Returns a string indicating the dog is barking."""
        return f'{self.name} barks'

    def run_speed(self):
        """Calcule et retourne la vitesse de course du chien."""
        return self.weight / self.age * 10

    def fight(self, other_dog):
        """Compare la puissance des deux chiens et déclare le vainqueur."""
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f'{self.name} wins the fight!'
        elif my_power == other_power:
            return "It's a tie!"
        else:
            return f'{other_dog.name} wins the fight!'


dog1 = Dog('Rex', 3, 30)
dog2 = Dog('Buddy', 5, 25)
dog3 = Dog('Max', 2, 20)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))