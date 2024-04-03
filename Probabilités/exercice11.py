import matplotlib.pyplot as plt

def compte(lettre, texte):
    compteur = 0
    for L in texte.lower():
        if L == lettre:
            compteur += 1
    return compteur

def frequences(texte):
    freq_dict = {}
    texte = texte.lower()
    for lettre in texte:
        if lettre.isalpha():
            if lettre in freq_dict:
                freq_dict[lettre] += 1
            else:
                freq_dict[lettre] = 1
    freq_list = list(freq_dict.items())
    freq_list.sort(key=lambda x: x[0])
    return freq_list

def afficher_diagramme(freq_list):
    lettres, frequences = zip(*freq_list)
    plt.bar(lettres, frequences)
    plt.xlabel('Lettres')
    plt.ylabel('Fréquences')
    plt.title('Diagramme en bâtons des fréquences d\'apparition des lettres')
    plt.show()
