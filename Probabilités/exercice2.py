import random

def simuler_jet_trois_des():
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    de3 = random.randint(1, 6)

    somme = de1 + de2 + de3

    print(f"Résultat du dé 1 : {de1}")
    print(f"Résultat du dé 2 : {de2}")
    print(f"Résultat du dé 3 : {de3}")
    print(f"Somme des trois dés : {somme}")

simuler_jet_trois_des()
