"""
@author: Ailton Domingues
"""

valor = float(input())

cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

if valor > 0 and valor < 10**6:  
    print("NOTAS:")
    for c in cedulas:
        restante = valor % c 
        nota = (valor - restante) / c
        valor = restante
        print(str(int(nota)) + " nota(s) de R$" , "%.2f" % round(c, 2))
        
    round(valor, 2)
    print("MOEDAS:")       
    for m in moedas:
        restante = valor % m
        moeda = (valor - restante) / m
        valor = restante
        print(str(int(moeda)) + " moeda(s) de R$" , "%.2f" % round(m, 2))