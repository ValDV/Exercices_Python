import random

def simuler_jet_de_pipe(nb_lancers):
    faces = [1, 2, 3, 4, 5, 6]
    probabilites = [0.10, 0.15, 0.15, 0.15, 0.15, 0.30]

    resultats = random.choices(faces, weights=probabilites, k=nb_lancers)

    for i, resultat in enumerate(resultats, start=1):
        print(f"Lancer {i}: {resultat}")

simuler_jet_de_pipe(100)
