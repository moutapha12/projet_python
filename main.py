
from gestion import ajouter_etudiant, afficher_etudiants
from statistiques import nombre_etudiants

def menu():
    while True:
        print("\n1. Ajouter étudiant")
        print("2. Afficher étudiants")
        print("3. Nombre étudiants")
        print("4. Quitter")

        choix = input("Choix: ")

        if choix == "1":
            nom = input("Nom: ")
            age = input("Age: ")
            ajouter_etudiant(nom, age)

        elif choix == "2":
            afficher_etudiants()

        elif choix == "3":
            print("Nombre:", nombre_etudiants())

        elif choix == "4":
            break

menu()
