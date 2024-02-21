import random

def constituer_groupes(eleves):
    random.shuffle(eleves)
    
    groupes = [eleves[i:i+3] for i in range(0, len(eleves), 3)]
    
    return groupes

eleves_classe = ["Élève1", "Élève2", "Élève3", "Élève4", "Élève5", "Élève6", "Élève7", "Élève8", "Élève9", "Élève10"]

groupes_formes = constituer_groupes(eleves_classe)

for i, groupe in enumerate(groupes_formes, start=1):
    print(f"Groupe {i}: {groupe}")
