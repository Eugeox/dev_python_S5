#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 08:48:59 2025

@author: guillian.durand
"""
from fonctions_date import is_a_date

date = input("Saisissez une date don le programme testera la validité (jj/mm/aaaa)\n")
d_m_y = date.split('/')
day = int(d_m_y[0])
month_nb = int(d_m_y[1])
year = int(d_m_y[2])
print("date valide") if is_a_date(day, month_nb, year) else print("date non valide")
