# coding: utf-8

def calcul_taux_periodique(taux_annuel, echeances_par_an=12):
    """
    >>> taux_annuel = 1.8
    >>> taux_mensuel = calcul_taux_periodique(taux_annuel)
    >>> taux_mensuel
    0.15
    """
    return taux_annuel / echeances_par_an


def calcul_interets(capital, taux_periodique):
    """
    Le capital emprunté est de 100€ :
    >>> capital = 100

    Le taux mensuel est :
    >>> taux_mensuel = calcul_taux_periodique(1.8)

    L'intérêt est :
    >>> calcul_interets(capital, taux_mensuel)
    15.0
    """
    return capital * taux_periodique

class TableauAmortissement:
    """
    Le capital emprunté est de 100€ :
    >>> capital = 100

    Le taux annuel est 2.4%:
    >>> taux_annuel = 2.4

    50€ sont remboursés par mois:
    >>> montant_echeances = 50

    >>> tableau = TableauAmortissement(capital, taux_annuel,
    ...                                montant_echeances)

    Le premier mois, 30€ sont remboursés sur les 100€, et 20€ d'euros sont
    payés (30€ + 20€ = 50€ payés par mois), il reste 70€ à remboursés.

    Il faut 3 mois pour tout remboursé.

    >>> tableau.affiche()
       Remboursé    Intérets     Restant
           30.00       20.00       70.00
           36.00       14.00       34.00
           34.00        6.80        0.00

    """

    def __init__(self, capital, taux_annuel, montant_echeances,
                 echeances_par_an=12):
        self.capital = capital
        self.taux_annuel = taux_annuel
        self.montant_echeances = montant_echeances
        self.echeances_par_an = echeances_par_an
        self.taux_periodique = calcul_taux_periodique(
            taux_annuel,
            echeances_par_an=echeances_par_an)

    def calcul(self):
        restant = self.capital
        while restant > 0:
            interets = calcul_interets(restant, self.taux_periodique)
            capital_rembourse = min(restant, self.montant_echeances - interets)
            restant -= capital_rembourse
            yield capital_rembourse, interets, restant

    def affiche(self):
        print('{:>12}{:>12}{:>12}'.format('Remboursé', 'Intérets', 'Restant'))
        for capital_rembourse, interets, capital in self.calcul():
            print('{:>12.2f}{:>12.2f}{:>12.2f}'.format(capital_rembourse, interets, capital))
