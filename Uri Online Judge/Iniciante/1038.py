"""
@author: Ailton Domingues
"""

c, q = [int(x) for x in input().split()]

tabela = {1 : 4.00, 2 : 4.50, 3 : 5.00, 4 : 2.00, 5 : 1.50}

print("Total: R$", "%.2f" % round((tabela[c]*q), 2))