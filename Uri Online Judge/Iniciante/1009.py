"""
@author: Ailton Domingues
"""

n = str(input())
s = float(input())
v = float(input())

t = s + (0.15 * v)

print("TOTAL = R$" , "%.2f" % round(t, 2))