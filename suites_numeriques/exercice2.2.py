import math

def premier_terme_sup_83000():
    v1 = 7
    q = 2
    n = 1
    vn = v1
    while vn < 83000:
        n += 1
        vn = v1 * q ** (n - 1)
    return n

print(f"Le premier rang pour lequel v_n ≥ 83000 est : {premier_terme_sup_83000()}")
