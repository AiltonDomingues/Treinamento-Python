"""
@author: Ailton Domingues
"""

import math

valor = float(input())

descontos = {range(0, 401) : 15, range(401, 801) : 12, range(801, 1201) : 10, range(1201, 2001) : 7}

if valor > 2000:
    reajuste = valor * 0.04
else:
    for r in descontos:
        if math.ceil(valor) in r: reajuste = valor * (descontos[r]) / 100

print("Novo salario:", "%.2f" % round((valor + reajuste), 2))
print("Reajuste ganho:", "%.2f" % round(reajuste, 2))
print("Em percentual:", "%.0f" % round((reajuste/valor)*100, 0), "%")