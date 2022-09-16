"""
@author: Ailton Domingues
"""

t = int(input())

a = t / (365)
m = t % (365) / 30
d = (t % 365) % 30

print(int(a), "ano(s)")
print(int(m), "mes(es)")
print(int(d), "dia(s)")