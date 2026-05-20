from datetime import date

def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def afficher_gateau(bougies):
    flammes = "i" * bougies
    bases   = "_" * bougies
    espaces = " " * (bougies // 2)

    print(f"      {espaces}___{flammes}___")
    print(f"      |:H:a:p:p:y:|")
    print(f"   ___|___________|___")
    print(f"   |^^^^^^^^^^^^^^^^^|")
    print(f"   |:B:i:r:t:h:d:a:y:|")
    print(f"   |                 |")
    print(f"   ~~~~~~~~~~~~~~~~~~~")

naissance = input("Entrez votre date de naissance (JJ/MM/AAAA) : ")
jour, mois, annee = map(int, naissance.split('/'))

aujourd_hui = date.today()
age = aujourd_hui.year - annee - ((aujourd_hui.month, aujourd_hui.day) < (mois, jour))

bougies = age % 10
if bougies == 0:
    bougies = 1

print(f"\nVous avez {age} ans — {bougies} bougie(s) sur votre gâteau !\n")

afficher_gateau(bougies)

if est_bissextile(annee):
    print("\nVous êtes né(e) une année bissextile ! Voici un deuxième gâteau !\n")
    afficher_gateau(bougies)