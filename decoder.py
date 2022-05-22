import os
import pickle


def decode(nom_du_fichier):
    """decode le fichier archive avec pickle"""
    os.chdir("C:\\Users\\thoma\\Documents\\GitHub\\Tipe")
    fichier = open(nom_du_fichier, "rb")
    l = pickle.load(fichier)
    fichier.close()
    return l

def encode(object, nom_du_fichier):
    """encode l'object dans un fichier avec pickle"""
    os.chdir("C:\\Users\\thoma\\Documents\\GitHub\\Tipe")
    fichier = open(nom_du_fichier, "wb")
    pickle.dump(object, fichier)
    fichier.close()
