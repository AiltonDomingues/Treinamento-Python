"""
@author: Ailton Domingues
"""

t = int(input())

h = t / (60*60)
m = t % (60*60) / 60
s = t % 60

print('{}:{}:{}'.format(int(h), int(m), s))