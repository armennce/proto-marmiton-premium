#fonctions inventaire aliments & outils

#----- INVENTAIRE ALIMENTS ------
def inventaire_aliments():
    print("1. aliments frais")
    print("2. aliments secs")
    print("3. aliments congelés")
    print("4. aliments en conserve")
    print("5. fruits")
    print("6. légumes")
    print("7. viandes")
    print("8. produits laitiers")

    while True:
        choix = input("Sélectionnez une catégorie d'aliments (1-8) ou 'Q' pour quitter : ")
        if choix == 'Q':
            break
        elif choix in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print(f"Vous avez sélectionné la catégorie {choix}.")
        else:
            print("Choix invalide. Veuillez réessayer.")

def menu_aliments():
    while True:
        print("\n--- Menu Aliments ---")
        print("1. Ajouter un aliment")
        print("2. Voir les aliments")
        print("3. Retour au menu principal")

        choix = input("Ton choix : ")
        if choix == "1":
            ajouter_aliment()
        elif choix == "2":
            afficher_aliments()
        elif choix == "3":
            break
        else:
            print("Choix invalide.")

def ajouter_aliment():
    nom = input("Nom de l’aliment : ")
    quantite = input("Quantité (ex: 2, 500g, etc.) : ")
    aliments[nom] = quantite

def afficher_aliments():
    if not aliments:
        print("Aucun aliment enregistré.")
    else:
        for nom, quantite in aliments.items():
            print(f"- {nom} : {quantite}")



#----- INVENTAIRE USTENSILS & OUTILS ------
def inventaire_ustensils_et_outils():
    print("1. batteur")
    print("2. mixeur")
    print("3. casserole")  
    print("4. poêle")
    print("5. rice cooker")
    print("6. four")
    print("7. planche")

    while True:
        pass

# ----- SOUS-MENU USTENSILES -----
def menu_ustensiles():
    while True:
        print("\n--- Menu Ustensiles ---")
        print("1. Ajouter un ustensile")
        print("2. Voir les ustensiles")
        print("3. Retour au menu principal")

        choix = input("Ton choix : ")
        if choix == "1":
            ustensile = input("Nom de l’ustensile : ")
            if ustensile not in ustensiles:
                ustensiles.append(ustensile)
        elif choix == "2":
            if not ustensiles:
                print("Aucun ustensile enregistré.")
            else:
                for u in ustensiles:
                    print(f"- {u}")
        elif choix == "3":
            break
        else:
            print("Choix invalide.")