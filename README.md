# Emprunt

Simulation d'emprunt bancaire

Note : Le développement est fait en français, car j'apprends les principes du
calcul de crédit avec les termes français. Ça pourrait éventuellement changer
par la suite.

Note : Tout est inspiré de l'[outil de simulation](http://www.cbanque.com/credit/simulateur.php)
de [cbanque.com](http://www.cbanque.com).

# Développement

### Installation des dépendances

Installer `Python 3.5` et `nose` dans un environnement `conda` :

    conda create -n emprunt python=3.5 nose
    source activate emprunt

    pip install -e .

# Tests

    nosetests
