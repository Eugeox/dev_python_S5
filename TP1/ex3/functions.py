#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 09:38:42 2025

@author: guillian.durand
"""

INDEX_IMPOTS = [(160336,45), (74546, 41), (26071, 30), (10226, 11), (0, 0)]
def mesImpots(revenue):
    """
    Parameters
    ----------
    revenue : int
        Les revenues soumis à l'impot

    Returns
    -------
    impots : int
        Les impots dus
    """
    impots = 0
    for i in range(len(INDEX_IMPOTS)):
        if revenue > INDEX_IMPOTS[i][0]:
            impots += (revenue-INDEX_IMPOTS[i][0])*INDEX_IMPOTS[i][1]/100
            revenue = INDEX_IMPOTS[i][0]
    return impots