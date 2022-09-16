"""
@author: Ailton Domingues
"""

a = float(input())
b = float(input())
c = float(input())

media = ((a*2) + (b*3) + (c*5))/10

print("MEDIA = " + str("{:.1f}".format(round(media, 1))))