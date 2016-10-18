# coding: utf-8

"""
Formules pour un taux actuariel

En France, utilisé pour les crédits autres que immobiliers, notamment les
crédits à la consommation.
"""

def calcul_taux_periodique(taux_annuel, echeances_par_an=12):
    """
    Avec annuel de 6% :
    >>> taux_annuel = 6

    Le taux mensuel est:
    >>> taux_mensuel = calcul_taux_periodique(taux_annuel)
    >>> print('{:.4}'.format(taux_mensuel))
    0.4868
    """
    return 100*(1 + 0.01*taux_annuel)**(1/echeances_par_an) - 100
