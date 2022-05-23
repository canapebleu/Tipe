import numpy as np

import decoder as d
import perceptron as p


def preparation_data(nom_du_fichier, proportion_train):
    datasets = d.decode(nom_du_fichier)
    n = len(datasets["data"])
    nombre_train = int(n*proportion_train)
    X_train = np.array(datasets["data"][:nombre_train])
    Y_train = np.array(datasets["target"][:nombre_train])
    X_test = np.array(datasets["data"][nombre_train:])
    Y_test = np.array(datasets["target"][nombre_train:])
    # on "applatit les matrices"
    X_train_reshape = X_train.reshape(X_train.shape[0], -1) / X_train.max()  # on normalise
    X_test_reshape = X_test.reshape(X_test.shape[0], -1) / X_train.max()  # on normalise
    return X_train_reshape, Y_train, X_test_reshape, Y_test


def trainning(nom_du_fichier,  learning_rate, n_iter, visualisation, proportion_train):
    X_train_reshape, Y_train, X_test_reshape, Y_test = preparation_data(nom_du_fichier, proportion_train)
    W, b = p.artificial_neuron(X_train_reshape, Y_train, X_test_reshape, Y_test, learning_rate, n_iter, visualisation)
    return W, b


def stocker_parametres(nom_du_fichier_datasets="datasets.txt", nom_du_fichier_parametres="parametres.txt", learning_rate=0.01, n_iter=10000, visualisation= True, proportion_train= 3/4):
    W, b = trainning(nom_du_fichier_datasets, learning_rate, n_iter, visualisation, proportion_train)
    d.encode([W, b], nom_du_fichier_parametres)

if __name__ == "__main__":
    stocker_parametres()