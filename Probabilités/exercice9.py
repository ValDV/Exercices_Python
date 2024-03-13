import random

def affichage():
    premier_chiffre = random.randint(1, 9)
    deuxieme_chiffre = random.randint(0, 9)
    troisieme_chiffre = random.randint(0, 9)
    
    return [premier_chiffre, deuxieme_chiffre, troisieme_chiffre]

def gain(partie):
    if partie[0] == partie[1] == partie[2]:
        return 50
    elif partie[0] == partie[1] - 1 == partie[2] - 2:
        return 20
    else:
        return 0

def gain_moyen(n):
    total_gain = 0
    for _ in range(n):
        partie = affichage()
        total_gain += gain(partie)
    return total_gain / n if n > 0 else 0

partie = affichage()
print("Résultat de la partie :", partie)
print("Gain de la partie :", gain(partie))

n = 1000
print(f"Gain moyen sur {n} parties :", gain_moyen(n))
