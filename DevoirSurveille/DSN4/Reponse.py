from typing import List


# Q3
def occupe(L: List[bool], i):
    return L[i]


# Q5
def egal(L1: List[bool], L2: List[bool]):
    if len(L1) != len(L2):
        return False
    else:
        for i in range(len(L1)):
            if L1[i] != L2[i]:
                return False
        return True


# Q9
def avancer_fin(L: List[bool], m: int):
    Lp = L[m:len(L - 1)]
    avancer(Lp, False)
    return L[0:m-1].extend(Lp)


#Q10
def avancer_debut(L: List[bool], b, m: int):
    Lp = L[0:m]
    avancer(Lp, b)
    return Lp.extend(L[m+1:len(L)-1])


#Q11
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
