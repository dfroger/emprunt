# coding: utf-8

def calcul_taux_periodique(taux_annuel, echeances_par_an=12):
    """
    >>> taux_annuel = 1.8
    >>> taux_mensuel = calcul_taux_periodique(taux_annuel)
    >>> taux_mensuel
    0.15
    """
    return taux_annuel / echeances_par_an

def calcul_interet(capital, taux_periodique):
    """
    Le capital restant à rembourser est de 100€ :
    >>> capital = 100

    Le taux mensuel est :
    >>> taux_mensuel = calcul_taux_periodique(1.8)

    L'intérêt est :
    >>> calcul_interet(capital, taux_mensuel)
    15.0
    """
    return capital * taux_periodique
