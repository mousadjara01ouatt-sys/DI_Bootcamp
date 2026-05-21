#Défi 1
mot = input("Entrez un mot : ")

dictionnaire = {}

for index, lettre in enumerate(mot):
    if lettre in dictionnaire:
        dictionnaire[lettre].append(index)
    else:
        dictionnaire[lettre] = [index]

print(dictionnaire)


#Défi 2
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

argent = int(wallet.replace("$", "").replace(",", ""))

basket = []

for article, prix in items_purchase.items():
    prix_propre = int(prix.replace("$", "").replace(",", ""))
    
    if prix_propre <= argent:
        basket.append(article)
        argent -= prix_propre

if basket == []:
    print("Nothing")
else:
    print(sorted(basket))