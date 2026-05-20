#Exercice1
mois = int(input("Entrez un numéro de mois (1-12) : "))
if mois >= 3 and mois <= 5:
    print(" Spring !")
elif mois >= 6 and mois <= 8:
    print(" Summer !")
elif mois >= 9 and mois <= 11:
    print(" Autumn !")
else:
    print(" Winter !")
    
    
 #Exercice2
for i in range(1, 21):
    print(i) 

for i in range(1, 21, 2):
    print(i)    
    
     
#Exercice3
nom = input("Entrez votre nom : ")
while nom != "OUATTARA":
    nom  = input("Entrez votre nom : ")
print("Bienvenue, OUATTARA !")


#Exercice4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Entrez votre nom : ")

if name in names:
    print(names.index(name))
else:
    print("Ce nom ne figure pas dans la liste.")


#Exercice5
n1 = int(input("Entrez le 1er nombre : "))
n2 = int(input("Entrez le 2ème nombre : "))
n3 = int(input("Entrez le 3ème nombre : "))

print(f"Le plus grand nombre est : {max(n1, n2, n3)}")



#Exercice6
import random

gagnees = 0
perdues = 0

while True:
    nombre_aleatoire = random.randint(1, 9)
    guess = int(input("Entrez un chiffre entre 1 et 9 : "))

    if guess == nombre_aleatoire:
        print("Gagnant !")
        gagnees += 1
    else:
        print(f"Bonne chance la prochaine fois. Le nombre était {nombre_aleatoire}.")
        perdues += 1

    continuer = input("Voulez-vous rejouer ? (oui/non) : ")
    if continuer.lower() != "oui":
        break

print(f"\nParties gagnées : {gagnees}")
print(f"Parties perdues : {perdues}")