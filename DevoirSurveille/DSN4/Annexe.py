def recherche(but, init):
    espace = [init]
    stop = False
    while not stop:
        ancien = espace
        espace = espace + successeurs(espace)
        espace.sort()  # Permet de trier espace par ordre croissant
        espace = elim_double(espace)
        stop = egal(ancien, espace)  # Fonction définie à la question 5
        if but in espace:
            return True
        return False


def in1(element, liste):
    a = 0
    b = len(liste)-1
    while(a <= b) and element >= liste[a]:
        if element == liste[a]:
            return True
        else:
            a = a + 1
    return False


def in2(element, liste):
    a = 0
    b = len(liste)-1
    while a < b:
        pivot = (a+b) // 2 # l'opérateur // est la division entière
        if liste[pivot] < element:
            a = pivot + 1
        else:
            b = pivot
    if element == liste[a]:
        return True
    else:
        return False


def versFile(n, taille):
    res = taille * [False]
    i = taille - 1
    while ...:
        if(n % 2) != 0:
            res[i] = True
        n = n // 2
        i = i - 1
    return res


def successeurs(L):
    res = []
    for x in L:
        L1 = x[0]
        L2 = x[1]
        res.append(avancer_files(L1, False, L2, False))
        res.append(avancer_files(L1, False, L2, True))
        res.append(avancer_files(L1, True, L2, False))
        res.append(avancer_files(L1, True, L2, True))
    return res


# Dans une liste triée, elim_double enlève les éléments apparaissent plus d'une fois
# Exemple : elim_double([1, 1, 2, 3, 3]) renvoie [1, 2, 3]
def elim_double(L):  # code à completer
    print('')


# Exemple d'utilisation
# Debut et fin sont des listes composées de deux files de même longueur impaire
# La première etant prioritaires par rapport à la seconde
debut = [5 * [False], 5 * [False]]
fin = [3 * [False] + 2 * [True], 3 * [False] + 2 * [True]]
print(recherche(fin, debut))
