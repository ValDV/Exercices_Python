def premier_rang_somme_1_million():
    u1 = 2
    r = 4
    n = 1
    somme = 0
    while somme < 1000000:
        un = u1 + (n - 1) * r
        somme = n * (u1 + un) // 2
        n += 1
    return n - 1

print(f"Le premier rang pour lequel la somme des termes est ≥ 1000000 est : {premier_rang_somme_1_million()}")
