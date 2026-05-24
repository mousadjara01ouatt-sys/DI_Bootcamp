import random


class Game:

    ITEMS = ["pierre", "papier", "ciseaux"]

    WINS_AGAINST = {
        "pierre": "ciseaux",
        "ciseaux": "papier",
        "papier": "pierre",
    }

    def get_user_item(self):
        while True:
            choix = input("Choisissez pierre, papier ou ciseaux : ").strip().lower()
            if choix in self.ITEMS:
                return choix
            print(f"Choix invalide '{choix}'. Veuillez entrer pierre, papier ou ciseaux.")

    def get_computer_item(self):
        return random.choice(self.ITEMS)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif self.WINS_AGAINST[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        result_messages = {
            "win":  "Vous avez gagne !",
            "draw": "Egalite !",
            "loss": "L'ordinateur a gagne. Vous avez perdu !",
        }

        print(f"\nVous avez choisi      : {user_item}")
        print(f"L'ordinateur a choisi : {computer_item}")
        print(result_messages[result])
        print()

        return result