"""
@author: Ailton Domingues
"""

import sys

lados = list([float(x) for x in input().split()])

maior = max(lados)
lados.remove(maior)

if maior >= sum(lados):
    print("NAO FORMA TRIANGULO")
    sys.exit()
if (maior**2) == (lados[0]**2 + lados[1]**2):
    print("TRIANGULO RETANGULO")
if (maior**2) > (lados[0]**2 + lados[1]**2):
    print("TRIANGULO OBTUSANGULO")
if (maior**2) < (lados[0]**2 + lados[1]**2):
    print("TRIANGULO ACUTANGULO")
if maior == lados[0] and maior == lados[1]:
    print("TRIANGULO EQUILATERO")
if maior == lados[0] != lados[1] or maior == lados[1] != lados[0] or lados[0] == lados[1] != maior:
    print("TRIANGULO ISOSCELES")