"""
@author: Ailton Domingues
"""

A = float(input())
B = float(input())

media = ((A*3.5) + (B*7.5))/11

print("MEDIA = " + str("{:.5f}".format(round(media, 5))))