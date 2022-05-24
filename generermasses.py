import os
import pickle
from tqdm import tqdm
import random

import masse as m
import utilitaire as u

os.chdir("C:\\Users\\thoma\\Documents\\GitHub\\Tipe")

# pour n = 64 on va fixer le seuil d'angulariter a m = 1/16 pour p = 64
# m = 1/8 equivaut a maligne
# m = 1/8 equivaut a benigne
# nom_du_fichier = "data.txt"


def genere_masse(entier, seuil, n, p):
    """genere une masse etiqueté avec une constante d'angularité deux fois superieur ou deux fois inferieur au seuil"""
    if entier == 1:
        return [m.masse(p, n, 2*seuil), entier]
    elif entier == 0:
        return [m.masse(p, n, seuil/2), entier]


def genere_masse2(entier, seuil, n, p):
    """genere une masse etiqueté avec une constante d'angularité plus ou moins aleatoire"""
    if entier == 1:
        const_angularite = random.gauss(seuil*2, seuil/4)
        return [m.masse(p, n, const_angularite), entier]
    elif entier == 0:
        const_angularite = random.gauss(seuil/2, seuil/4)
        return [m.masse(p, n, const_angularite), entier]


def stocker_masses(nombres_images, seuil, n, p, nom_du_fichier="datasets.txt"):
    """stock les matrices d'images de masses etiquetés dans un fichier data.txt dans le meme dossier"""
    masses = {"data": [], "target": []}
    for i in tqdm(range(nombres_images)):
        entier = random.randint(0, 1)
        masse = genere_masse2(entier, seuil, n, p)
        masses["data"].append(masse[0])
        masses["target"].append(masse[1])
        u.encode(masses, nom_du_fichier)


if __name__ == "__main__":
    stocker_masses(500, 1/16, 64, 64, "datasets.txt")
