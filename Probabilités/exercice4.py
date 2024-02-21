import random

def simuler_jets_deux_des(nb_simulations):
    for i in range(nb_simulations):
        de1 = random.randint(1, 8)
        de2 = random.randint(1, 8)

        somme = de1 + de2

        print(f"Simulation {i + 1}: Somme des deux dés : {somme}")

simuler_jets_deux_des(200)
