def calcul_terme_n(n):
    u1 = 2
    r = 4
    un = u1 + (n - 1) * r
    return un

n = int(input("Entrez la valeur de n : "))
print(f"Le terme u_{n} est : {calcul_terme_n(n)}")
