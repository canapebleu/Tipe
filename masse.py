import random

import matplotlib.pyplot as plt
import numpy as np

import utilitaire as u

# r = 0.375 * n le rayon de la masse avec n la taille de l'image
# c = (int(n/2),int(n/2)) le centre de l'image
# on defini m = 1/8  la constante d'angularité un nombre qui qui quantifie les imperfections a la surface de la masse


def init_image(n):
    """initialisation d'une image"""
    return np.zeros((n, n), dtype=np.uint8)


def IJ2XY(v, n):
    """changement de base pour s'adapter aux matrices"""
    p = int(n/2)
    x = v[1] - p
    y = -v[0] + p
    return x, y

def IJ2XY_decentre(v, n, v_translation):
    """changement de base pour s'adapter aux matrices en decentrant les masses"""
    x_translation, y_translation = v_translation[0], v_translation[1]
    p = int(n/2)
    x = v[1] - p + x_translation
    y = -v[0] + p + y_translation
    return x, y

def translation_aleatoire(n, sigma = 1):
    """retourne un vecteur de direction et de norme aleatoire"""
    x_translation = random.gauss(0, sigma) * 1/12 * n
    y_translation = random.gauss(0, sigma) * 1/12 * n
    return x_translation, y_translation

def liste_des_points_du_cercle(p, r):
    """renvoie p points du cercle de centre (0,0) de rayon r repartis comme il faut"""
    points = []
    pi = np.pi
    for i in range(p):
        teta = (2*pi*i)/p
        x = r*np.cos(teta)
        y = r*np.sin(teta)
        points.append((x, y))
    return points


def sommet(v, m):
    """on veut associer un sommet a un point du cercle"""
    a = random.gauss(0, 1)
    x0, y0 = v
    x = x0 * (1 + a*m)
    y = y0 * (1 + a*m)
    return x, y


def liste_sommets(p, r, m):
    """renvoie les coordonnées de p points disposés aleatoirement avec la constante d'angularité m autour d'un cercle de rayon r de centre (0,0)"""
    l0 = liste_des_points_du_cercle(p, r)
    l = []
    for ell in l0:
        l.append(sommet(ell, m))
    return l


def point_in_polygone(v, liste):
    """teste si le point v est dans le polygone lié a la liste ordonnée de points liste"""
    p = len(liste)
    for i in range(p):
        M = v
        A = 0, 0
        B = liste[i % p]
        C = liste[(i+1) % p]
        pv1 = (A[0] - M[0])*(B[1]-M[1]) - (A[1]-M[1])*(B[0] - M[0])
        pv2 = (B[0] - M[0])*(C[1]-M[1]) - (B[1]-M[1])*(C[0] - M[0])
        pv3 = (C[0] - M[0])*(A[1]-M[1]) - (C[1]-M[1])*(A[0] - M[0])
        if pv1*pv2 >= 0 and pv1*pv3 >= 0 and pv2*pv3 >= 0:
            return True
    return False


def rayon_min_max(liste):
    """determine les rayons des envelloppes circulaires du polygones pour l'optimisation"""
    rayon_min = np.sqrt(liste[0][0]**2+liste[0][1]**2)
    rayon_max = np.sqrt(liste[0][0]**2+liste[0][1]**2)
    for k in range(len(liste)):
        a = np.sqrt(liste[k][0]**2+liste[k][1]**2)
        rayon_min = min(rayon_min, a)
        rayon_max = max(rayon_max, a)
    return rayon_min, rayon_max


def masse(p, n, m):
    """renvoie la matrice d'une masse de rayon r=0.375 * n de constante d'angularité m avec p points d'angularité"""
    image = init_image(n)
    r = 0.375 * n
    l = liste_sommets(p, r, m)
    rayon_min, rayon_max = rayon_min_max(l)
    translation = translation_aleatoire(n)
    #translation = (0, 0)
    for i in range(n):
        for j in range(n):
            v = IJ2XY_decentre((i, j), n, translation)
            x, y = v
            b = np.sqrt(x**2+y**2)
            if b <= rayon_min:
                image[i, j] = 255
            elif b <= rayon_max:
                if point_in_polygone(v, l):
                    image[i, j] = 255
    return image


if __name__ == "__main__":
    u.show(masse(64, 64, 1/16))

