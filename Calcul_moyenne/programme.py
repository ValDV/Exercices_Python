def moyenne(tab: list) -> float:
    '''
    Fonction moyenne : Prend un tableau de valeurs en paramètre et en retourne la moyenne de ses valeurs.
    '''
    return sum(tab) / len(tab)

def minimum(tab: list) -> float:
    '''
    Fonction minimum : Prend un tableau de valeurs en paramètre et en retourne la valeur minimale.
    '''
    return min(tab)

def maximum(tab: list) -> float:
    '''
    Fonction maximum : Prend un tableau de valeurs en paramètre et en retourne la valeur maximale.
    '''
    return max(tab)

def etendue(tab: list) -> float:
    '''
    Fonction etendue : Prend un tableau de valeurs en paramètre et en retourne l'étendue des valeurs.
    '''
    return max(tab) - min(tab)

def mediane(tab: list) -> float:
    '''
    Fonction mediane : Prend un tableau de valeurs en paramètre et en retourne la valeur médiane.
    '''
    sorted_tab = sorted(tab)
    n = len(sorted_tab)
    if n % 2 == 0:
        middle1 = sorted_tab[n // 2]
        middle2 = sorted_tab[n // 2 - 1]
        return (middle1 + middle2) / 2
    else:
        return sorted_tab[n // 2]

# Initialisation des valeurs minimale et maximale en secondes
min_time = float("inf")
max_time = float("-inf")

times = []  # Liste pour stocker les temps en secondes

for i in range(4):  # Répéter 10 fois
    time_input = input("Veuillez entrer un temps (minutes:secondes) : ")  # Demander à l'utilisateur de rentrer le temps

    # Diviser le temps entré en minutes et secondes
    minutes, seconds = map(int, time_input.split(":"))

    # Convertir le temps en secondes et l'ajouter à la liste
    time_in_seconds = minutes * 60 + seconds
    times.append(time_in_seconds)

    # Mettre à jour les valeurs minimale et maximale
    if time_in_seconds < min_time:
        min_time = time_in_seconds
    if time_in_seconds > max_time:
        max_time = time_in_seconds

# Utilisation des fonctions pour calculer les statistiques
average_seconds = moyenne(times)
min_seconds = minimum(times)
max_seconds = maximum(times)
range_seconds = etendue(times)
median_seconds = mediane(times)

print(f"La moyenne des temps est de {average_seconds} secondes")
print(f"Le temps minimum est {min_seconds} secondes")
print(f"Le temps maximum est {max_seconds} secondes")
print(f"L'étendue des temps est de {range_seconds} secondes")
print(f"La médiane des temps est de {median_seconds} secondes")
