#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 11:27:27 2025

@author: guillian.durand
"""
"""
TODO: trouver le max
"""
from functions import *

#print(Syracuse_recursif(int(input("Quel nombre ?"))))

#x = int(input("Quel nombre ?"))

#Syracuse(x)
#print(f"Altitude maximal: {Altitude(x)}")
#print(f"Temps de vol: {tmpVol(x)}")

tmpVol_max = 0
tmpVol_max_index = 0
alt_max = 0
alt_max_index = 0

for i in range(1000):
    if tmpVol(i) > tmpVol_max:
        tmpVol_max = tmpVol(i)
        tmpVol_max_index = i
    if Altitude(i) > alt_max:
        alt_max = Altitude(i)
        alt_max_index = i
    print(i)
print(f"Pour les nombres entre 1 et 1000 le temps de vol le plus long est {tmpVol_max} pour {tmpVol_max_index}")
print(f"Pour les nombres entre 1 et 1000 l'altitude maximale est {alt_max} pour {alt_max_index}")
    