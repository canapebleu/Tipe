import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from tqdm import tqdm


def initialisation(X):
    """initialisation des parametre W et b du preceptron"""
    W = np.random.randn(X.shape[1])
    b = np.random.randn(1)
    return (W, b)


def model(X, W, b):
    """forward propagation"""
    Z = X.dot(W) + b
    A = 1 / (1 + np.exp(-Z))
    return A


def log_loss(A, y):
    """fonction coût que l'on va tenter de minimiser"""
    epsilon = 1e-15  # pour eviter les log(0)
    return 1 / len(y) * np.sum(-y * np.log(A + epsilon) - (1 - y) * np.log(1 - A + epsilon))


def gradients(A, X, y):
    """calcule les gradients de la fonctions coût"""
    dW = 1 / len(y) * np.dot(X.T, A - y)
    db = 1 / len(y) * np.sum(A - y)
    return (dW, db)


def update(dW, db, W, b, learning_rate):
    """calcul de W(i+1) et b(i+1) par avec la methode de la descente du gradient"""
    W = W - learning_rate * dW
    b = b - learning_rate * db
    return (W, b)


def predict(X, W, b):
    """fonction qui renvoie le booléen de la prediction à l'aide du model"""
    A = model(X, W, b)
    return A >= 0.5


def artificial_neuron(X_train, y_train, X_test, y_test, learning_rate, n_iter, visualisation):
    """perceptron"""
    W, b = initialisation(X_train)

    if visualisation:
        train_loss = []
        train_acc = []
        test_loss = []
        test_acc = []

    for i in tqdm(range(n_iter)):
        A = model(X_train, W, b)

        if visualisation:
            # Train
            train_loss.append(log_loss(A, y_train))
            y_pred = predict(X_train, W, b)
            train_acc.append(accuracy_score(y_train, y_pred))

            # Test
            A_test = model(X_test, W, b)
            test_loss.append(log_loss(A_test, y_test))
            y_pred = predict(X_test, W, b)
            test_acc.append(accuracy_score(y_test, y_pred))

        # mise a jour
        dW, db = gradients(A, X_train, y_train)
        W, b = update(dW, db, W, b, learning_rate)

    if visualisation:
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.plot(train_loss, label='train LogLoss')
        plt.plot(test_loss, label='test LogLoss')
        plt.legend()
        plt.subplot(1, 2, 2)
        plt.plot(train_acc, label='train accuracy')
        plt.plot(test_acc, label='test accuracy')
        plt.legend()
        plt.show()

    return (W, b)
