#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 09:55:09 2025

@author: guillian.durand
"""
from functions import mesImpots

revenues = input("Quels sont vos revenues ?")
print(f"Les impots sur votre revenu s'élèvent a {mesImpots(int(revenues))}")

