#Défi 1
number = int(input("Entrez un nombre : "))
length = int(input("Entrez une longueur : "))

multiples = [number * i for i in range(1, length + 1)]

print(f"number: {number} - length {length} → {multiples}")

#Défi 2

word = input("Entrez une chaîne : ")

result = ""
for i in range(len(word)):
    if i == 0 or word[i] != word[i - 1]:
        result += word[i]

print(f'user\'s word : "{word}" → "{result}"')