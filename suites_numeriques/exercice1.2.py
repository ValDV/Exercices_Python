def premier_terme_sup_55000():
    u1 = 2
    r = 4
    n = 1
    un = u1
    while un < 55000:
        n += 1
        un = u1 + (n - 1) * r
    return n

print(f"Le premier rang pour lequel u_n ≥ 55000 est : {premier_terme_sup_55000()}")
