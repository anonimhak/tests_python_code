from sys import argv, stdout
import math
from random import randint
from typing import List
from my_functions import print_table_dict


def poligon_chastot(l: List[int]):
    poligon = {}
    for i in l:
        if not i in poligon:
            poligon[i] = 1
        else:
            poligon[i] += 1
    return poligon

def get_mediana(l: List[int]):
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        i1 = len(l) // 2 -1
        i2 = i1 + 1
        return (l[i1] + l[i2]) / 2

def get_indexs(l):
    l2 = []
    for i in l:
        if not i in l2:
            l2.append(i)
    l2 = sorted(l2)
    return l2

def get_len(l: List[int]):
    return len(get_indexs(l))

def get_megi(l: List[int]):
    i = get_indexs(l)
    return (min(i), max(i))

if __name__ == "__main__":
    #l = [randint(35, 45) for i in range(41)]
#    l = [6, 7, 9, 12, 4, 5, 12, 9, 9, 8, 10, 10, 7, 9, 9, 8, 4,
#        5, 6, 8, 8, 9, 10, 5, 7, 6, 9, 5, 5, 7, 9, 10, 10, 7, 9, 12, 4, 5,
#        8, 7, 8, 9, 10, 11, 7, 6, 10, 7, 9, 11, 4, 9, 8, 10, 10, 12]
    l = [
        7, 7, 9, 12, 4, 5, 11, 11, 12, 9, 9, 9, 10, 10, 7, 9, 9, 8, 4, 5, 8, 8, 8, 9, 10, 11, 7, 6, 9, 5, 5, 12, 9, 10, 10, 7, 9, 12, 4, 5, 11, 7, 8,
        9, 10, 11, 7, 6, 9, 8, 10, 7, 9, 12, 4, 9, 8, 10, 10, 12, 11, 12, 9, 10, 7, 7, 7, 4, 7
    ]
    print(sorted(l))
    p = poligon_chastot(l)
    print_table_dict(p)
    print("Медіана:  "+str(get_mediana(l)))
    print("Мода:     "+str(get_len(l)))
    megi = get_megi(l)
    print("Межі:     "+str(megi[0])+", "+str(megi[1]))
    print(len(l))
    print(l[35])
