"""
@author: Ailton Domingues
"""

valor = int(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]

if valor > 0 and valor < 10**6:  
    print(valor)
    for c in cedulas:
        restante = valor % c 
        notas = (valor - restante) / c
        valor = restante
        print(str(int(notas)) + " nota(s) de R$ " + str(c) + ",00")