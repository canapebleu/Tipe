import numpy as np

import utilitaire as u
import perceptron as p
import reseau_multicouche as r


def preparation_data(nom_du_fichier, proportion_train):
    datasets = u.decode(nom_du_fichier)
    n = len(datasets["data"])
    nombre_train = int(n*proportion_train)
    X_train = np.array(datasets["data"][:nombre_train])
    Y_train = np.array(datasets["target"][:nombre_train])
    X_test = np.array(datasets["data"][nombre_train:])
    Y_test = np.array(datasets["target"][nombre_train:])
    # on "applatit les matrices"
    X_train_reshape = X_train.reshape(
        X_train.shape[0], -1) / X_train.max()  # on normalise
    X_test_reshape = X_test.reshape(
        X_test.shape[0], -1) / X_train.max()  # on normalise
    return X_train_reshape, Y_train, X_test_reshape, Y_test


def trainning(nom_du_fichier, learning_rate, n_iter, visualisation, proportion_train):
    X_train_reshape, Y_train, X_test_reshape, Y_test = preparation_data(
        nom_du_fichier, proportion_train)
    W, b = p.artificial_neuron(
        X_train_reshape, Y_train, X_test_reshape, Y_test, learning_rate, n_iter, visualisation)
    return W, b


def stocker_parametres(nom_du_fichier_datasets="datasets.txt", nom_du_fichier_parametres="parametres.txt", learning_rate=0.01, n_iter=10000, visualisation=True, proportion_train=3/4):
    W, b = trainning(nom_du_fichier_datasets, learning_rate,
                     n_iter, visualisation, proportion_train)
    u.encode([W, b], nom_du_fichier_parametres)


def preparation_data_multicouche(nom_du_fichier, proportion_train):
    datasets = u.decode(nom_du_fichier)
    n = len(datasets["data"])
    nombre_train = int(n*proportion_train)
    X_train = np.array(datasets["data"][:nombre_train])
    Y_train = np.array(datasets["target"][:nombre_train])
    X_test = np.array(datasets["data"][nombre_train:])
    Y_test = np.array(datasets["target"][nombre_train:])
    # on "applatit les matrices"
    X_train_reshape = X_train.reshape(
        X_train.shape[0], -1) / X_train.max()  # on normalise
    X_test_reshape = X_test.reshape(
        X_test.shape[0], -1) / X_train.max()  # on normalise
    # on transpose les vecteurs
    X_train_reshape_transpose = X_train_reshape.T
    X_test_reshape_transpose = X_test_reshape.T
    Y_train_reshape = Y_train.reshape((1, Y_train.shape[0]))
    Y_test_reshape = Y_test.reshape((1, Y_test.shape[0]))

    return X_train_reshape_transpose, Y_train_reshape, X_test_reshape_transpose, Y_test_reshape


def trainning_multicouche(nom_du_fichier, hidden_layers, learning_rate, n_iter, visualisation, proportion_train):
    X_train, Y_train, X_test, Y_test = preparation_data_multicouche(
        nom_du_fichier, proportion_train)
    parametres = r.deep_neural_network(
        X_train, Y_train, hidden_layers, learning_rate, n_iter, visualisation)

    return parametres


def stocker_parametres_multicouche(nom_du_fichier_datasets="datasets.txt", nom_du_fichier_parametres="parametres2.txt", hidden_layers=(16, 16, 16), learning_rate=0.001, n_iter=3000, visualisation=True, proportion_train=3/4):
    parametres = trainning_multicouche(nom_du_fichier_datasets, hidden_layers,
                                       learning_rate, n_iter, visualisation, proportion_train)
    u.encode(parametres, nom_du_fichier_parametres)


if __name__ == "__main__":
    stocker_parametres()
    #stocker_parametres_multicouche()
