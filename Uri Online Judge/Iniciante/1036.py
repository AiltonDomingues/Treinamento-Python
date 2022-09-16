"""
@author: Ailton Domingues
"""

a, b, c = [float(x) for x in input().split()]

d = (b**2) - 4*a*c

if a <= 0 or d < 0:
    print("Impossivel calcular")
else:
    r1 = (-b + d ** (1/2)) / (2*a)
    r2 = (-b - d ** (1/2)) / (2*a)

    print("R1 =", "%.5f" % round(r1, 5))
    print("R2 =", "%.5f" % round(r2, 5))