import random

def lancer_de_pipe():
    probabilites = [0.1252, 0.1309, 0.2157, 0.1987, 0.1123, 0.2172]

    resultat = random.choices(range(1, 7), probabilites)[0]
    
    return resultat

resultat_jet = lancer_de_pipe()
print("Le résultat du jet de dé est :", resultat_jet)
