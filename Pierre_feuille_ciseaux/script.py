# Importation de la fonction 'choice' depuis le module 'random'
from random import choice

# Définition d'une liste contenant les options du jeu
liste_signes = ["pierre", "feuille", "ciseaux"]

# L'ordinateur choisit aléatoirement un signe parmi la liste
signe_ordi = choice(liste_signes)

# Le joueur entre son choix (pierre, feuille ou ciseaux)
signe_joueur = input("Choisissez pierre, feuille ou ciseaux :")

# Conversion du choix du joueur en minuscules pour éviter des problèmes de compréhension par la machine
signe_joueur = signe_joueur.lower()

# Affichage du choix du joueur
print("Vous avez choisi", signe_joueur)

# Affichage du choix de l'ordinateur
print("L'Ordinateur a choisi", signe_ordi)

# Si les deux choix sont identiques, il y a égalité
if signe_ordi == signe_joueur:
    print("Egalite")

# Si une de ces conditions se réalise, le joueur gagne
elif signe_joueur == "pierre" and signe_ordi == "ciseaux":
    print("Victoire Joueur")

elif signe_joueur == "feuille" and signe_ordi == "pierre":
    print("Victoire Joueur")

elif signe_joueur == "ciseaux" and signe_ordi == "feuille":
    print("Victoire Joueur")

# Si aucune des conditions précédentes se réalise, c'est l'ordinateur qui gagne
else:
    print("Victoire Ordinateur")