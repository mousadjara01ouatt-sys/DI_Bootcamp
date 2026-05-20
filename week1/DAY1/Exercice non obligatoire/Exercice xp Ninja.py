#Exercice1
3 <= 3 < 9 # True

3 == 3 == 3 # True

bool(0) # False
bool(5 == "5") # False
bool(4 == 4) == bool("4" == "4") # True
bool(bool(None)) # False

x = (1 == True) # True
y = (1 == False) # False
a = True + 4 # True est traité comme 1, donc a vaut 5
b = False + 10 # False est traité comme 0, donc b vaut 10

print("x is", x) # True
print("y is", y) # False
print("a:", a) # 5
print("b:", b) # 10

#Exercice2

record = 0

while True:
    phrase = input("Entrez une phrase sans le caractère 'A' : ")

    if 'a' in phrase.lower():
        print("Phrase invalide ! Elle contient la lettre 'A'.")
    elif len(phrase) > record:
        record = len(phrase)
        print(f"Félicitations ! Nouveau record : {record} caractères !")
    else:
        print(f"Pas de nouveau record. Record actuel : {record} caractères.")
        
        
#Exercice3
paragraphe = """L'intelligence artificielle est une technologie qui transforme notre monde à une vitesse impressionnante. 
Elle permet aux machines d'apprendre, de raisonner et de prendre des décisions comme le ferait un être humain. 
Aujourd'hui, l'IA est présente dans notre quotidien : recommandations de films, assistants vocaux, voitures autonomes. 
Les chercheurs du monde entier travaillent sans relâche pour repousser les limites de cette technologie fascinante. 
L'avenir de l'intelligence artificielle soulève des questions importantes sur l'éthique et l'impact social."""

mots = paragraphe.split()
phrases = [p.strip() for p in paragraphe.replace('!', '.').replace('?', '.').split('.') if p.strip()]
mots_uniques = set(mot.lower().strip('.,!?:;') for mot in mots)
mots_non_uniques = len(mots) - len(mots_uniques)
sans_espaces = paragraphe.replace(' ', '').replace('\n', '')
mots_par_phrase = len(mots) / len(phrases)

print("=" * 50)
print("        ANALYSE DU PARAGRAPHE")
print("=" * 50)
print(f"Nombre de caractères          : {len(paragraphe)}")
print(f"Nombre de caractères (sans espaces) : {len(sans_espaces)}")
print(f"Nombre de phrases             : {len(phrases)}")
print(f"Nombre de mots                : {len(mots)}")
print(f"Nombre de mots uniques        : {len(mots_uniques)}")
print(f"Nombre de mots non uniques    : {mots_non_uniques}")
print(f"Moyenne de mots par phrase    : {mots_par_phrase:.1f}")
print("=" * 50)
        