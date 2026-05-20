# Exercice 1
print('Hello world\n' * 4)

## Exercice 2 
result = (99**3) * 8
print(result)

# Exercice 3
print(5 < 3)    # False
print(3 == 3)   # True
print(3 == "3") # False
print("3" > 3) # TypeError 
print("Hello" == "hello") # False

# Exercice 4
computer_brand = "HP"
print("I have a " + computer_brand + " computer.")

# Exercice 5
name = "OUATTARA"
age = 22
shoe_size = 40
info = f"Je m'appelle {name}, j'ai {age} ans et je chausse du {shoe_size}."
print(info)

# Exercice 6
a = 10
b = 5

if a > b:
    print("Hello World")

# Exercice 7
nombre = int(input("Entrez un nombre : "))

if nombre % 2 == 0:
    print(f"{nombre} est pair.")
else:
    print(f"{nombre} est impair.")

# Exercice 8
mon_nom = "Ouattara"
nom_utilisateur = input("Comment tu t'appelles ? ")

if nom_utilisateur.lower() == mon_nom.lower():
    print(f"Incroyable ! Tu t'appelles aussi {nom_utilisateur} ? On est des jumelles !")
else:
    print(f"Enchanté {nom_utilisateur} ! Moi c'est {mon_nom}, on n'est pas jumelles mais on peut être amis !")

# Exercice 9
hauteur = int(input("Quelle est ta hauteur en centimètres ? "))

if hauteur > 145:
    print("Tu es assez grand pour y monter !")
else:
    print("Tu n'es pas assez grand, tu dois encore grandir pour pouvoir rouler !")