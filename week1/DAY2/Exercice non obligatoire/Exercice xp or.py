#Exercice 1
birthdays = {
    "Adjara": "2004/05/14",
    "Ouattara": "2003/08/22",
    "Penie": "2006/03/07",
    "Papouni": "2001/11/19",
    "Mamouni": "1999/06/30"
}

print("Bienvenue !")
print("Vous pouvez chercher les dates de naissance des personnes sur la liste !")

nom = input("Entrez le nom d'une personne : ")

if nom in birthdays:
    print(f"La date de naissance de {nom} est : {birthdays[nom]}")
else:
    print(f"{nom} n'est pas dans la liste.")
    
#Exercice 2
birthdays = {
    "Adjara": "2004/05/14",
    "Ouattara": "2003/08/22",
    "Penie": "2006/03/07",
    "Papouni": "2001/11/19",
    "Mamouni": "1999/06/30"
}

print("Bienvenue !")
print("Vous pouvez chercher les dates de naissance des personnes sur la liste !")

print("Personnes disponibles :")
for nom in birthdays:
    print(f"- {nom}")

nom = input("Entrez le nom d'une personne : ")

if nom in birthdays:
    print(f"La date de naissance de {nom} est : {birthdays[nom]}")
else:
    print("Désolé, nous n'avons pas les informations de date de naissance.")
    
    
#Exercice 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

nom = input("Entrez votre nom : ")

if nom in names:
    print(f"L'index de la première apparition de {nom} est : {names.index(nom)}")
else:
    print(f"{nom} n'est pas dans la liste.")
    
    #Exercice 4
import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    count = 0
    while True:
        de1 = throw_dice()
        de2 = throw_dice()
        count += 1
        if de1 == de2:
            return count

def main():
    resultats = []
    for i in range(100):
        resultats.append(throw_until_doubles())
    
    total = sum(resultats)
    moyenne = total / len(resultats)
    
    print(f"Total throws: {total}")
    print(f"Average throws to reach doubles: {round(moyenne, 2)}.")

main()
     