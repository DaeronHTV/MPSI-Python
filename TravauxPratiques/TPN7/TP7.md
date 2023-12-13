# TP I.P.T 7 - Algorithmes Usuels

Le fichier TP7.py contient deux listes :

- La liste **mois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 
'novembre', 'décembre']** pour l'exercice 1
- Une liste **test** de 100 chiffres choisis aléatoirement pour les exercices 2 à 4

## 1. Affichage de date

La liste des mois est fournie.

1. Ecrire une fonction **Date(j,m,a)** qui renvoie la date avec le mois écrit en lettres: j est le jour, m le mois et a
l'année.
2. Modifier la fonction précédente pour qu'elle affiche les années sur 4 chiffres si la date est comprise entre le 1er
janvier 1921 et le 31 décembre 2020

## 2. Recherche d'un élément

La liste test est fournie pour tester l'éxécution de vos fonctions.

1. Ecrire une fonction **recherche(x, liste)** qui renvoie **True** ou **False** selon que **x** est oui ou non un des
éléments de liste;
2. Il peut être intéressant de déterminer la position à laquelle se trouve l'élément recherché. Ecrire une fonction
**indice(x,liste)** qui renvoie le premier i tel que **liste[i] = x**. La fonction renverra -1 si l'élément n'est pas trouvé.
3. Ecrire une fonction **indiceFinal(x,liste)** qui renvoie le dernier indice i tel que **liste[x] = x**
4. Ecrire une fonction **indices(x,liste)** qui renvoie la liste de tous les indices de tous les indices i tel que
**liste[i] = x**

## 3. Moyenne et Variance

La liste **test** est fournie pour tester l'éxécution de vos fonctions.

1. Ecrire une fonction **moyenne(liste)** qui renvoie la moyenne des éléments contenues dans la liste.
2. Ecrire une fonction **moyenne_pond(liste)** qui renvoie la moyenne des éléments contenus dans liste, chaque valeur
**liste[i]** étant présente avec l'effectif partiel correspondant à la valeur de l'élément précédent **liste[i-1]**
   (pour le premier élément, l'effectif partiel associé correspond donc à la valeur contenue dans le dernier élément de
la liste)

## 4. Tri par sélection dans une liste

La liste **test_tri** est fournie pour tester l'éxécution de vos fonctions.

On cherche dans cet exercice à implémenter une fonction de tri par séléction. Cette méthode consiste à travailler sur deux
listes: la liste des éléments triés et celle des éléments à tier. A chaque itération, on cherchera le plus petit élement
de la liste des éléments à trier, puis on l'extraira et on le placera à la fin de la liste des éléments triés, jusqu'à
ce que la liste des éléments à trier soit vide.

1. Ecrire une fonction **min(L)** retournant l'indice **K** de l'élément le plus petit de L.
2. Ecrire une fonction **retire(L,i)** retire **L[i]** de **L** et renvoie sa valeur (on pourra placer l'élément à la fin de la liste
et utiliser pop)
3. Ecrire une fonction **tri_selection(L)** retournant un tableau trié par ordre croissant des éléments de **L**
4. A l'aide des fonctions **duree(f,x)** et **list_rand(n)** présentes dans le fichier TP5.py, tracer le temps d'éxécution
moyen de la fonction **tri_selection(L)** en fonction de **n** le nombre d'éléments de la liste.
5. Comparer graphiquement le résultat obtenu à la question précédente avec celui obtenu à l'aide de la fonction 
**sorted(L)** nativement présente dans Python.