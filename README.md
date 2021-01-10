# Avila Dataset
Groupe DIA3:
Gabot Quentin
Hansen Cédric 

## Contenu
Le dataset contient des informations sur la calligraphie de phrases dans une bible ancienne, comme la distance entre la marge du haut, la distance entre chaque colonne, ou encore la taille des pointes des chiffres. Pour chaque regroupement de 3 phrases, on sait quelle scribe à écrit cette partie. Ces derniers sont dénotés par les:
['A','B','C','D','E','F','G','H','I','X','Y','Z']

## But du projet
Le but du projet est de determiner à l'aides des valeurs dans chaque variables quel scribe à écrit quel partie du text.
Pour ce faire le dataset est découper en 2, la première partie correspond est utiliser pour train notre modèle prédictif quand à la deuxième partie
cela correspondra à notre dataset à tester.

## Resultat
Au travers du projet nous explorons plusieurs modèles predictif de Machine Learning.
Notre meilleur modèle est un Random Forest avec une accuraccy de 99.95%

## Fonctionnement de l'API
Pour faire marcher l'API flask il faut (dans le répertoire du fichier)
activer l'environnement avec la commande:
``` bash
./monenv/Scripts/activate
```
``` bash
pip install -r requirements.txt 
```
``` python
python app.py
```

