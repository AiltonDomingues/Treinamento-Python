"""
@author: Ailton Domingues
"""

a, b, c = list([float(x) for x in input().split()])

if a < (b + c) and b < (a + c) and c < (a + b):
    print("Perimetro =", "%.1f" % round((a + b + c), 1))
else:
    print("Area =", "%.1f" % round(((a + b)*c) / 2, 1))