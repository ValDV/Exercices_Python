import random

eleves = ["Élève1", "Élève2", "Élève3", "Élève4", "Élève5", "Élève6", "Élève7", "Élève8", "Élève9", "Élève10",
          "Élève11", "Élève12", "Élève13", "Élève14", "Élève15", "Élève16", "Élève17", "Élève18", "Élève19", "Élève20",
          "Élève21", "Élève22", "Élève23"]

random.shuffle(eleves)

groupes = [eleves[i:i+3] for i in range(0, len(eleves), 3)]

for i, groupe in enumerate(groupes, start=1):
    print(f"Groupe {i}: {', '.join(groupe)}")
