#EXERCICE1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

resultat = dict(zip(keys, values))

print(resultat)

#EXERCICE2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


total = 0


for name, age in family.items():
    
   
    if age < 3:
        prix = 0
        print(name + " : Gratuit")
    
  
    elif age <= 12:
        prix = 10
        print(name + " : 10$")
    
  
    else:
        prix = 15
        print(name + " : 15$")
    

    total += prix


print("Total : " + str(total) + "$")



#EXERCICE3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}
brand.update({"number_stores": 2})
print("Zara vend des vetements pour : " + str(brand["type_of_clothes"]))
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand)

brand.pop("creation_date")

print("Dernier competitor : " + brand["international_competitors"][-1])

print("Couleurs aux US : " + str(brand["major_color"]["US"]))

print("Nombre de cles : " + str(len(brand)))

print("Toutes les cles : " + str(list(brand.keys())))

#EXERCICE4

def describe_city(city, country="Unknown"):
    print(city + " is in " + country + ".")

describe_city("Reykjavik", "Iceland")

describe_city("Paris")

#EXERCICE5

import random
def compare_numbers(number):
    random_number = random.randint(1, 100)
    if number == random_number:
            print("Success!")
    else:
        print("Fail! Your number: " + str(number) + ", Random number: " + str(random_number))
compare_numbers(50)


#EXERCICE6

def make_shirt(size="large", text="I love Python"):
    print("The size of the shirt is " + size + " and the text is " + text + ".")
   
make_shirt()

make_shirt(size="medium")
4
make_shirt(size="small", text="Custom message")

#EXERCICE7
import random
def get_random_temp():
    return random.randint(-10, 40)
def main():
     temperature = get_random_temp()
     print("The temperature right now is " + str(temperature) + " degrees Celsius.")
     if temperature < 0:
        print("Brrr, c'est glacial ! Mets des couches supplementaires aujourd'hui.")
    
     elif temperature <= 16:
        print("Il fait assez frais ! N'oublie pas ton manteau.")
    
     elif temperature <= 23:
        print("Beau temps.")
    
     elif temperature <= 32:
        print("Un peu chaud, restez hydrate.")
    
     else:
        print("Il fait vraiment chaud ! Reste calme.")
main()

#EXERCICE8
garnitures = []
counter = 0

while True:
    
    garniture = input('entrer les garnitures une par une : ')
    if garniture == 'quit':
        break
    garnitures.append(garniture)
    
    print("Adding [" + garniture + "] to your pizza.")

print("Your pizza has the following garnitures: " + str(garnitures))

for x in garnitures:
    counter += 1

total_price = 10 + counter * 2.50
print("Le prix total de la pizza est: " + str(total_price) + " $.")
    





    



















import random

# On genere une temperature aleatoire entre -10 et 40


# La fonction principale

    
    # On recupere la temperature aleatoire
   
    
    # On affiche la temperature
    
    
    # On donne des conseils selon la temperature
    