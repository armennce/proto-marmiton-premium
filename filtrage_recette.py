#fonctions pour filtrer recettes

#----- TROUVER UNE RECETTE ------
def trouver_recette():
    print("1. entrée")
    print("2. plat")
    print("3. dessert")
    print("4. boisson")

    while True:
        pass

# ----- RECETTE -----
def proposer_recette():
    print("\n🔍 On cherche une recette adaptée...")
    if "œufs" in aliments and "farine" in aliments:
        print("Tu peux faire une crêpe 🥞 !")
    else:
        print("Désolé, pas assez d’ingrédients pour une recette connue 😔.")