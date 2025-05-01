aliments = {}
ustensiles = []

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Gérer les aliments")
        print("2. Gérer les ustensiles")
        print("3. Proposer une recette")
        print("4. Quitter")

        choix = input("Ton choix : ")
        if choix == "1":
            menu_aliments()
        elif choix == "2":
            menu_ustensiles()
        elif choix == "3":
            proposer_recette()
        elif choix == "4":
            print("À bientôt 🍽️ !")
            break
        else:
            print("Choix invalide.")

# ----- SOUS-MENU ALIMENTS -----
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

# ----- RECETTE -----
def proposer_recette():
    print("\n🔍 On cherche une recette adaptée...")
    if "œufs" in aliments and "farine" in aliments:
        print("Tu peux faire une crêpe 🥞 !")
    else:
        print("Désolé, pas assez d’ingrédients pour une recette connue 😔.")

# Lancer l’app
menu_principal()



#----- SAUVEGARDE DONNÉES AVEC JSON ------
#1. sauvegarder les données dans un fichier JSON
import json

def sauvegarder_aliments(fichier="aliments.json"):
    with open(fichier, "w") as f:
        json.dump(aliments, f, indent=4)
    print("✅ Aliments sauvegardés.")

#2. charger les données au démarrage 
def charger_aliments(fichier="aliments.json"):
    global aliments
    try:
        with open(fichier, "r") as f:
            aliments = json.load(f)
        print("✅ Aliments chargés.")
    except FileNotFoundError:
        aliments = {}  # Si le fichier n'existe pas encore

