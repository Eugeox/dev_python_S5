#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 10:21:53 2025

@author: guillian.durand
"""

def matriceMult_3x3(A, B):
    C =[[0,0,0],[0,0,0],[0,0,0]]
    
    for i in range(len(A)): #3
        for j in range(len(A[0])): #3
            for k in range(3):
                C[i][j] += A[i][k]*B[k][j]
    return C

def matriceMult(A, B):
    """
    Parameters
    ----------
    A : tableau de tableaux
        La matrice A
    B : tableau de tableaux
        La matrice B

    Returns
    -------
    C : tableau de tableaux
        La matrice tel que C = A * B
    """
    assert len(A[0]) == len(B), "Le produit des deux matrices n'est pas réalisable"
    C = [[0 for i in range(len(B[0]))] for j in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C
