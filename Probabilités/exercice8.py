import random

def de_urne():
    d = random.randint(1, 6)
    
    if d == 6:
        u = random.randint(1, 10)
    else:
        u = random.randint(1, 20)
    
    if u == 1:
        return "Le joueur a gagné"
    else:
        return "Le joueur a perdu"

resultat = de_urne()
print(resultat)
