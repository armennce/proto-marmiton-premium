#fonctions de sauvegarde données


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
