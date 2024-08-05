# Yam's en Python

## Utilisation

Télécharger tous les fichiers dans un même dossier. **Python 3.10+ est nécessaire**

Pour lancer le jeu

```
python main.py
```

## Règles du jeu

### But du jeu
Vous devez marquer le plus de points possible en faisant des combinaisons avec les 5 dés. Vous avez trois lancers, avec la possibilité de conserver des dés d'un lancer sur l'autre, ou de s'arrêter et marquer un score à tout moment. Si vous ne pouvez ou ne voulez rien marquer à l'issue des trois tirages, vous pouvez décider de barrer une case, càd de renoncer à un coup en espérant mieux réussir après.

### Liste des coups
Il y a 13 coups :
 - **1 :** somme des dés de valeur 1
 - **2 à 6 :** idem
 - **Brelan :** 3 dés identiques (somme des 5 dés)
 - **Carré :** 4 dés identiques (somme des 5 dés)
 - **Full :** 3 dés et 2 dés respectivement identiques (25 pts)
 - **Petite suite :** 4 dés dont les valeurs se suivent (30 pts)
 - **Grande suite :** 5 dés dont les valeurs se suivent (40 pts)
 - **Yam's :** 5 dés identiques (50 pts)
 - **Chance :** combinaison quelconque (somme des 5 dés)

### Comptage des points
A la fin de la partie, on additionne les points des coups 1 à 6 pour former le premier sous-total, auquel s'ajoute un bonus de 35 points si celui-ci est supérieur ou égal à 63 (score obtenu avec 3 dés dans chacun des coups). Le deuxième sous-total s'obtient en additionnant les points de tous les autres coups (un coup barré ne vaut aucun point). La somme des deux sous-totaux forme le score final qui détermine le podium.

## Graphisme

Pour l'instant, seule l'interface dans le shell est disponible.

## IA

Aucune IA n'est disponible pour le moment
