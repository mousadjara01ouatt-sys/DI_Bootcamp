#Défi 1
def create_letter_index(word):
    letter_indices = {}
    
    for index, letter in enumerate(word):
        if letter in letter_indices:
            letter_indices[letter].append(index)
        else:
            letter_indices[letter] = [index]
    
    return letter_indices

word = input("Enter a word: ")
print(create_letter_index(word))


#Défi 2
def find_affordable_items(items, wallet_str):
    wallet_amount = int(wallet_str.replace("$", "").replace(",", ""))
    
    basket = []
    
    for item, price in items.items():
        clean_price = int(price.replace("$", "").replace(",", ""))
        
        if clean_price <= wallet_amount:
            basket.append(item)
            wallet_amount -= clean_price
    
    if basket == []:
        return "Nothing"
    else:
        return sorted(basket)

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
print(find_affordable_items(items_purchase, wallet))