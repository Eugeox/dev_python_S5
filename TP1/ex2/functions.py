# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 08:48:59 2025

@author: guillian.durand
"""

def is_bissextile(year):
    """
    Parameters
    ----------
    year : int
        On test si l'année est bissextile

    Returns
    -------
    True or False

    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_in_month(month_nb, year):
    """

    Parameters
    ----------
    month_nb : int
        compris enre 1 et 12 correspond a un mois de l'année
    year : int
        correspond à l'année, qui nous permetra de determiner 
            le nombre de jours en fevrier'

    Returns 
    -------
    str
        message d'erreur
    int
        nombre de jours

    """
    if month_nb < 0 or month_nb >12:
        return "Choose a valid month number (1 -> 12)"
    else:
        if month_nb == 2:
            return 29 if is_bissextile(year) else 28
        else:
            if month_nb in [1, 3, 5, 7, 8, 10, 12]:
                return 31
            else:
                return 30
            
def is_a_date(day, month_nb, year): 
    """
    Parameters
    ----------
    day : int
        jour du mois
    month_nb : int
        numéro correspondant au mois de l'année'
    year : int
        année
    Returns
    -------
    True si les assert sont validés

    """
    assert 0 < month_nb <= 12, "date non valide" #f"Le {month_nb}ième mois n'est pas un numéro valide"
    assert 0 < day <= day_in_month(month_nb, year), "date non valide" #f"Le {day}ième jour n'est pas un jour valide"
    return True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
