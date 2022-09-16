"""
@author: Ailton Domingues
"""

import math

hi, mi, hf, mf = [int(x) for x in input().split()]

hi = hi + (mi / 60)
hf = hf + (mf / 60)

if hi >= hf: duracao = 24 - (hi - hf)
else: duracao = abs(hi - hf)

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(math.floor(duracao), round((duracao % 1)*60)))