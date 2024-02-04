def resol_eq_seconde_degre (a,b,c):
    if a !=0
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Il n'y a pas de solution réelle."
        elif delta == 0:
            x = -b / (2*a)
            return ("Il y a une solution réelle: " + str(x))
        else:
            x1 = (-b - sqrt(delta)) / (2*a)
            x2 = (-b + sqrt(delta)) / (2*a)
            return ("Il y a deux solutions réelles:" + str(x1) + " et ")
    else:
        return ("a = 0. Ce n'est pas une fonction de second degré.")
