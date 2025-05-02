#main menu

def menu_principal():
    print("Bienvenue dans l'application Marmiton Premium !")
    print("-----MENU PRINCIPAL-----")  
    print("1. inventaire aliments")
    print("2. inventaire ustensils & outils de cuisines")
    print("3. trouver une recette")
    print("4. créer un profil")
    print("5. créer une recette")
    print("6. Quitter")

    while True:
        
        choix = input("Sélectionnez une option (1-6) ou 'Q' pour quitter : ")
        if choix == '1':
            inventaire_aliments()
        elif choix == '2':
            inventaire_ustensils_et_outils()
        elif choix == '3':
            trouver_recette()
        elif choix == '4':
            creer_profil()
        elif choix == '5':
            pass  # Fonctionnalité à implémenter
        elif choix == 'Q':
            print("Merci d'avoir utilisé Marmiton Premium ! À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")



aliments = {}
ustensiles = []


# Lancer l’app
menu_principal()


