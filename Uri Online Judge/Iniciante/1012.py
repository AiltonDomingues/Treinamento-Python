"""
@author: Ailton Domingues
"""

a, b, c = [float(x) for x in input().split()]

pi = 3.14159

t, c, tr, q, r = (a*c)/2, pi*(c**2), ((a+b)*c)/2, b**2, a*b


print("TRIANGULO:" , "%.3f" % round(t, 3))
print("CIRCULO:" , "%.3f" % round(c, 3))
print("TRAPEZIO:" , "%.3f" % round(tr, 3))
print("QUADRADO:" , "%.3f" % round(q, 3))
print("RETANGULO:" , "%.3f" % round(r, 3))