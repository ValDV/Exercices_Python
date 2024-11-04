def calcul_terme_n(n):
    v1 = 7
    q = 2
    vn = v1 * q ** (n - 1)
    return vn

n = int(input("Entrez la valeur de n : "))
print(f"Le terme v_{n} est : {calcul_terme_n(n)}")
