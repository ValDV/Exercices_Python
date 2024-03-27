from random import*
def monte_carlo():
    n=1000
    c=0
    for i in range(n):
        x=random()
        y=random()
        if x**2+y**2 < 1:
            c+=1
    return 4*c/n