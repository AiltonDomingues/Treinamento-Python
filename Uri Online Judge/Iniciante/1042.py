"""
@author: Ailton Domingues
"""

v = list([int(x) for x in input().split()])
copia = v.copy()

for i in range(len(v)): 
    menor = min(v)
    print(menor)
    v.remove(menor)
    
print("")   
print(*copia, sep='\n')