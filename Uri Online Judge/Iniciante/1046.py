"""
@author: Ailton Domingues
"""

hi, hf = [int(x) for x in input().split()]

if hi >= hf: duracao = 24 - (hi - hf)
else: duracao = abs(hi - hf)

print("O JOGO DUROU {} HORA(S)".format(duracao))