def somme_termes_jusqu_a_n(n):
    v1 = 7
    q = 2
    somme = v1 * (q ** n - 1) // (q - 1)
    return somme

n = int(input("Entrez la valeur de n : "))
print(f"La somme des termes jusqu'au rang {n} est : {somme_termes_jusqu_a_n(n)}")
