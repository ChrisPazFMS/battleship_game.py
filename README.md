# Projet de Bataille Navale en Python

## Description

Ce projet est une implémentation du jeu de Bataille Navale en Python. Le jeu indique au joueur après chaque tir si celui-ci est tombé dans l'eau, a touché un navire et, dans ce cas, si ce navire est coulé. La partie se termine lorsque tous les navires sont coulés.

## Comment jouer

Pour jouer à ce jeu, exécutez le fichier `battleship_game.py` avec Python 3. Vous serez invité à entrer vos coordonnées de tir sous la forme "LettreNombre" (par exemple, "A1"). Le jeu vous informera du résultat de chaque tir.

## Gestion des erreurs

Le programme comprend une gestion d'erreur pour la saisie de l'utilisateur. Si l'utilisateur entre une coordonnée qui n'est pas valide, le programme affiche un message d'erreur et demande à l'utilisateur de réessayer.

## Développement

Ce projet est en cours de développement. Les futures mises à jour incluront des améliorations de l'interface utilisateur et de la logique du jeu.

## Version actuelle

La version actuelle du jeu comprend la logique de base du jeu de Bataille Navale, y compris la définition des navires, la saisie des tirs par l'utilisateur, la vérification des tirs et la détermination de la fin de la partie.

## Prochaines étapes

Les prochaines étapes du développement de ce projet incluent :

- **Factorisation du code** : Le code actuel est écrit en mode déclaratif. La prochaine étape sera de factoriser le code pour passer en mode fonctionnel. Cela impliquera de définir des fonctions pour différentes parties de la logique du jeu, comme la vérification des tirs, la détermination si un navire est coulé, et la détermination de la fin de la partie.

- **Amélioration de l'affichage de la grille** : Actuellement, le jeu n'affiche pas la grille après chaque tir. Une future mise à jour inclura un affichage de la grille après chaque tir, avec des caractères représentant l'état de chaque case.

- **Interface utilisateur graphique** : Actuellement, le jeu se joue dans la console. Une interface utilisateur graphique rendrait le jeu plus attrayant et plus facile à utiliser.

- **Jouer contre l'ordinateur** : Pour l'instant, le jeu est un jeu solo où le joueur tire sur des navires statiques. Une fonctionnalité intéressante à ajouter serait la possibilité de jouer contre l'ordinateur, qui placerait ses navires de manière aléatoire et tirerait également de manière aléatoire.

## Suites possibles

En fonction du temps disponible, il sera possible d'explorer ces suites possibles de l'exercice :

- Placer aléatoirement les bateaux au démarrage.
- Rendre variable le nombre de lignes et de colonnes de la grille.
- Séparer le programme en plusieurs modules.
