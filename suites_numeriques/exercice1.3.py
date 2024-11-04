def somme_termes_jusqu_a_n(n):
    u1 = 2
    r = 4
    un = u1 + (n - 1) * r
    somme = n * (u1 + un) // 2
    return somme

n = int(input("Entrez la valeur de n : "))
print(f"La somme des termes jusqu'au rang {n} est : {somme_termes_jusqu_a_n(n)}")
