def premier_rang_somme_1_234_567():
    v1 = 7
    q = 2
    n = 1
    somme = 0
    while somme < 1234567:
        somme = v1 * (q ** n - 1) // (q - 1)
        n += 1
    return n - 1 

print(f"Le premier rang pour lequel la somme des termes est ≥ 1234567 est : {premier_rang_somme_1_234_567()}")
