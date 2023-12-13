# Devoir Surveillé 4 - Réponses

## I. Préliminaires

1. Expliquer comment représenter une file de voitures à l'aide d'une liste de booléens

On considère une liste booléen de taille n tel que n = nb cases de la file. On peut représenter la file de voiture avec
une liste de ce type car on a la même taille que la file et la valeur booléen indique la présence ou non d'une voiture
dans la case
- True : Une voiture est présente dans la case 
- False : Il n'y a pas de voiture dans la case<br/>

Ce qui donne pour exemple : L[i] = True avec 0 <= i < len(L) indique que la case i de la file de voiture contient une
voiture

2. Donner une ou plusieurs instructions Python permettant de définir une liste A représentant la file de voiture 
illustrée sur la Figure 1.

```python
#Premiere instruction
L = [True, False, True, True, False, False, False, False, False, False, True]
#Deuxieme instruction
L = []
L.append(True)
L.append(False)
# ...
```

3. Soit L une liste représentant une file de longueur n et i un entier tel que 0 <= i < n. Définir en python la fonction
occupe(L,i) renvoyant True lorsque la case d'indice i de la file est occupée par une voiture et False sinon.

```python
from typing import List

def occupe(L: List[bool], i):
    return L[i]
```

4. Combien existe-t-il de files différentes de longueur n ? justifier votre réponse

Point sur les données actuelles :
- On sait qu'une file est de longueur n avec n € N<sup>*</sup><sub>+</sub>
- On sait qu'un element de la liste peut prendre deux valeurs distinctes (True or False)

Ce qui implique qu'il y a **2<sup>n</sup>** possibiltés pour une file de voitures de longueur n (sachant qu'il n'y a pas
contraintes sur les relations entre L[i] et L[i+1], Exemple : il n'y pas avoir plus de trois cases True d'affilée sur 
une file)

5. Ecrire une fonction egal(L1,L2) retournant un booleen permettant de savoir si deux listes L1 et L2 sont égales. 
On s'interdira d'utiliser l'instruction L1 == L2

```python
from typing import List

def egal(L1: List[bool], L2: List[bool]):
    if len(L1) != len(L2):
        return False
    else:
        for i in range(len(L1)):
            if L1[i] != L2[i]:
                return False
        return True
```

6. Que peut-on dire de la compléxité de cette fonction

Note :
- Ici la fonction la plus couteuses est la boucle for car on va parcourir l'ensemble des deux listes pour comparer les 
valeurs
- On a également les if et else mais c'est dernier c'est très peu couteux comparé à notre boucle for
- Les opération if/else/opérateur sont en O(1)
- Les boucles for sont en minimum en O(n) avec n la longueur de la file

=> La complexité de l'algorithme donné pour répondre est égale à O(n)

7. Préciser le type de retour de cette fonction

On retourne une valeur booléenne. True indique que les listes sont de même longueur et que les valeurs sont identiques à
chaque position. False indique qu'au moins une des deux conditions précédemment évoquée n'est pas respectée.

## II. Déplacement de voitures dans une file

8. Etant donnée A une liste définie question 2, que renvoie **avancer(avancer(A, False), True) ?

```python
#Liste de base
L = [True, False, True, True, False, False, False, False, False, False, True]
#avancer(A,False)
L = [False, True, False, True, True, False, False, False, False, False, False]
#avancer(avancer(A,False),True)
L = [True, False, True, False, True, True, False, False, False, False, False]
```

9. On considère L une liste et m l'indice d'une de cette liste (0 <= m < len(L)). On s'intéresse à une étape partielle 
où seules les voitures situées sur la case d'indice m ou à droite de cette case peuvent avancer normalement, les 
autres voitures ne se déplaçant pas.

```python
from typing import List

def avancer_fin(L:List[bool],m:int):
    Lp = L[m:len(L-1)]
    avancer(Lp, False)
    return L[0:m-1].extend(Lp)
```

10. Définir la fonction avancer_debut(L,b,m) qui réalise cette étape partielle de déplacement et renvoie le résultat 
dans une nouvelle liste sans modifier L.

```python
from typing import List

def avancer_debut(L: List[bool], b, m: int):
    Lp = L[0:m]
    avancer(Lp, b)
    return Lp.extend(L[m+1:len(L)-1])
```

11. Définir la fonction avancer_debut_bloque(L,b,m) qui réalise cette étape partielle de déplacement et renvoie le 
résultat dans une nouvelle liste.

On considère que la fonction avancer déjà écrite ne fait pas avancer une voiture si jamais cette dernière ne peut pas 
avancer. (Pourquoi ? Il n'y a pas de précision dans l'énoncé pour répondre clairement à la question donc on peut
considérer ce que l'on veut)

```python
def avancer_debut_bloque(L,b,m):
    Lp = L[0:m-1]
    i = len(Lp)-1
    while i != 0:
        if not(Lp[i]) and Lp[i-1]: #Bloque l'affection si Lp[i-1] == False mais est-ce plus optimisé ?
            Lp[i] = Lp[i-1]
        i = i - 1
    if not(Lp[0]) and b:
        Lp[0] = b
    return Lp + L[m:len(L-1)]
```