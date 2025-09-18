#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 11:14:41 2025

@author: guillian.durand
"""

def Syracuse_recursif(x):
    """
    Parameters
    ----------
    x : int
        nombre de la suite

    Returns
    -------
    int
        revoie dans la fonction de maniere recursive

    """
    print(x)
    if x == 1:
        return 1
    if x&1:
        return Syracuse_recursif(x*3+1)
    else:
        return Syracuse_recursif(x//2)



def Syracuse(x):
    """
    Parameters
    ----------
    x : int
        Premier terme de la serie de Syracuse

    Returns
    -------
    None.

    """
    vol = 0
    max = 0
    while x !=1:
        print(x)
        vol += 1
        if x >= max:
            max = x
        if x&1:
            x = 3*x + 1
        else:
            x = x // 2
    print(f"Altitude maximal: {max}")
    print(f"Temps de vol: {vol}")



def tmpVol(x):
    """
    Parameters
    ----------
    x : int
        Premier terme de la serie de Syracuse

    Returns
    -------
    vol : int
        Le temps de vol de la suite en fonction de x

    """
    vol = 0
    while x !=1:
        vol += 1
        if x&1:
            x = 3*x + 1
        else:
            x = x // 2
    return vol



def Altitude(x):
    """
    Parameters
    ----------
    x : int
        Premier terme de la serie de Syracuse

    Returns
    -------
    max : int
        L'altitude maximale atteinte par la suite de Syracuse en fonction de x

    """
    max = 0
    while x !=1:
        if x >= max:
            max = x
        if x&1:
            x = 3*x + 1
        else:
            x = x // 2
    return max