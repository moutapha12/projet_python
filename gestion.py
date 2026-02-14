from database import ajouter, afficher

def ajouter_etudiant(nom, age):
    ajouter(nom, age)
    print("Etudiant ajouté")

def afficher_etudiants():
    for e in afficher():
        print(e["nom"], e["age"])
