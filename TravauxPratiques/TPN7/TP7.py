import random
from typing import List

def random_list(nombre):
    _: List[int] = []
    i: int = 0
    while i < nombre:
        _.append(random.randint())
        i = i + 1
    return _


mois: List[str] = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'décembre']
test = random_list(100)

