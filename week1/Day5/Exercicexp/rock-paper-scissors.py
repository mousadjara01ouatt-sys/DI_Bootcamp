from game import Game


def get_user_menu_choice():
    print("=" * 40)
    print("   PIERRE, PAPIER, CISEAUX")
    print("=" * 40)
    print("  [1] Jouer une nouvelle partie")
    print("  [2] Afficher les scores")
    print("  [q] Quitter")
    print("=" * 40)

    choix = input("Votre choix : ").strip().lower()

    if choix not in ("1", "2", "q"):
        print(f"Option '{choix}' invalide. Choisissez 1, 2 ou q.\n")

    return choix


def print_results(results):
    total = results["win"] + results["loss"] + results["draw"]

    print("\n" + "=" * 40)
    print("        RESUME DES PARTIES")
    print("=" * 40)
    print(f"  Parties jouees  : {total}")
    print(f"  Victoires       : {results['win']}")
    print(f"  Defaites        : {results['loss']}")
    print(f"  Egalites        : {results['draw']}")
    print("=" * 40)
    print("Merci d'avoir joue ! A bientot.")
    print("=" * 40 + "\n")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choix = get_user_menu_choice()

        if choix == "1":
            partie = Game()
            resultat = partie.play()
            results[resultat] += 1

        elif choix == "2":
            print_results(results)

        elif choix == "q":
            print_results(results)
            break


if __name__ == "__main__":
    main()