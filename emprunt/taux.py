def taux_periodique(taux_annuel, echeances_par_an=12):
    """
    >>> taux_annuel = 1.8
    >>> taux_mensuel = taux_periodique(taux_annuel)
    >>> taux_mensuel
    0.15
    """
    return taux_annuel / echeances_par_an
