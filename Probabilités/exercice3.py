import random

def simuler_jets_trois_des(nb_simulations):
    for i in range(nb_simulations):
        de1 = random.randint(1, 6)
        de2 = random.randint(1, 6)
        de3 = random.randint(1, 6)

        somme = de1 + de2 + de3

        print(f"Simulation {i + 1}: Somme des trois dés : {somme}")

simuler_jets_trois_des(50)
