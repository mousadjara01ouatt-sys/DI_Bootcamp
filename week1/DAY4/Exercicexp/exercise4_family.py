class Person:
    def __init__(self, first_name, age):
        """Initialise une personne avec un prénom et un âge."""
        self.first_name = first_name
        self.age = age
        self.last_name = ''

    def is_18(self):
        """Retourne True si la personne a 18 ans ou plus."""
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        """Initialise une famille avec un nom de famille."""
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        """Ajoute un nouveau membre à la famille."""
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        """Vérifie si un membre de la famille est majeur."""
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print('You are over 18, your parents Jane and John accept that you will go out with your friends')
                else:
                    print('Sorry, you are not allowed to go out with your friends.')
                return
        print(f'No member named {first_name} found in the family.')

    def family_presentation(self):
        """Présente tous les membres de la famille."""
        print(f'Family name: {self.last_name}')
        for member in self.members:
            print(f'{member.first_name}, {member.age} years old')


my_family = Family('Smith')
my_family.born('Alice', 20)
my_family.born('Tom', 15)
my_family.born('Emma', 18)

my_family.check_majority('Alice')
my_family.check_majority('Tom')
my_family.check_majority('Kevin')
my_family.family_presentation()