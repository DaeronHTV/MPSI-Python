# Devoir Surveillé 4 - Etude de trafic routier

On s'intéresse à la conception d'un logiciel d'étude de trafic routier modélisant le déplacement d'un ensemble de
voitures sur des files à sens unique (voir Figure 1 et 2). C'est un schéma simple qui permet de comprendre l'apparition
d'embouteillage et de concevoir des solutions pour fluidifier le trafic.<br/>
On notera, pour L une liste:
- len(L) sa longueur
- L[i] l'élément d'indice i pour <= i < len(L)
- L[i:j] une sous liste composé des éléments L[i],...,L[j] pour 0 <= i < j <= len(L)
- p x L avec p € N<sup>*</sup> la liste obtenue en concatenant p fois la liste L. Par exemple, 3*[0] est la liste [0,0,0]

***TODO - Mettre les figures***

## I. Préliminaires

Dans un premier temps, on considère le cas d'une seule file illustré Figure 1. Une file de longueur n est représentée
par n cases. Une case peut contenir au plus une voiture. Les voitures présentes dans une file circulent dans le même sens
(sens des indices croissants, représenté par des flèches sur les illustrations) et sont différenciées.

1. Expliquer comment représenter une file de voitures à l'aide d'une liste de booléens
2. Donner une ou plusieurs instructions Python permettant de définir une liste A représentant la file de voiture illustrée
sur la Figure 1.
3. Soit **L** une liste représentant une file de longueur n et i un entier tel que 0 <= i < n. Définir en python la
fonction **occupe(L,i)** renvoyant **True** lorsque la case d'indice i de la file est occupée par une voiture et **False**
sinon.
4. Combien existe-t-il de files différentes de longueur n ? justifier votre réponse
5. Ecrire une fonction **egal(L1,L2)** retournant un booleen permettant de savoir si deux listes **L1** et **L2** sont
égales. On s'interdira d'utiliser l'instruction **L1 == L2**
6. Que peut-on dire de la compléxité de cette fonction
7. Préciser le type de retour de cette fonction

## II. Déplacement de voitures dans une file

On identifie désormais une file de voitures à une liste. On considère les schémas Figure 3 représentant des exemples de
files. Une étape de simulation pour une file consiste à déplacer les voitures de la file à tour de rôle, en commançant
par la voiture la plus à droite selon les règles suivantes :

- Une voiture se trouvant sur la case la plus à droite de la file sort de la file
- Une voiture peut avancer d'une case vers la droite si elle arrive sur une case inoccupée
- Une case libérée par une voiture devient inoccupée.
- La case la plus à gauche peut devenir occupée ou non selon le cas considéré

On suppose avoir écrit en python la fonction avancer prenant en paramètres une liste de départ, un booléen indiquant si
la case la plus à gauche doit devenir occupée lors de l'étape de la simulation, et renvoyant la liste obtenue par une
étape de simulation.<br/>
Par exemple, l'application de cette fonction à la liste illustrée par la Figure 3(a) permet d'obtenir soit la liste
illustrée par la Figure 3(b) lorsque l'on considère qu'aucune voiture nouvelle n'est introduite, soit la liste illustrée
par la Figure 3(c) lorsque l'on considère qu'une voiture nouvelle est introduite.

***TODO - faire les figures***

8. Etant donnée A une liste définie question 2, que renvoie **avancer(avancer(A, False), True) ?
9. On considère L une liste et m l'indice d'une de cette liste (0 <= m < len(L)). On s'intéresse à une étape partielle
où seules les voitures situées sur la case d'indice m ou à droite de cette case peuvent avancer normalement, les autres
voitures ne se déplaçant pas.<br/>
***TODO - Faire les figures*** <br/>
Définir en Python la fonction avancer_fin(L, m) qui réalise cette étape partielle de déplacement et renvoie le résultat
dans une nouvelle liste sans modifier L.
10. Soient L une liste, b un booléen et m l'indice d'une case inoccupée de cette liste. On considère une étape partielle
où seules les voitures situées sur à gauche de la case d'indice m se déplaçant, les autres voitures ne se déplaçant pas.
Le booléen b indique si une nouvelle voiture est introduite sur la case la plus à gauche.<br/>
***TODO - Faire les figures*** <br/>
lorque aucune nouvelle voiture n'est introduite.<br/>
Définir la fonction avancer_debut(L,b,m) qui réalise cette étape partielle de déplacement et renvoie le résultat dans
une nouvelle liste sans modifier L.
11. On considère une liste L dont la case d'indice m > 0 est temporairement inaccessible et bloque l'avancée des voitures.
Une voiture située immédiatement à gauche de la cas d'indice m ne peut avancer. Les voitures situées sur les cases plus
à gauche peuvent avancer, à moins d'êtres bloquées par une case introduite lorsque cela est possible.<br/>
***TODO - Faire les figures*** <br/>
lorsqu'aucune nouvelle voiture n'est introduite.<br/>
Définir la fonction avancer_debut_bloque(L,b,m) qui réalise cette étape partielle de déplacement et renvoie le résultat
dans une nouvelle liste.


## III. Une étape de simulation à deux files

## IV. Transitions

## V. Atteignabilité

