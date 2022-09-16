"""
@author: Ailton Domingues
"""

c1, n1, v1 = input().split()
c2, n2, v2 = input().split()

v = int(n1) * float(v1) + int(n2) * float(v2)

print("VALOR A PAGAR: R$" , "%.2f" % round(v, 2))