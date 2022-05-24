import utilitaire as u
import numpy as np

def decode_reshape_W(nom_du_fichier):
    W = np.array(u.decode(nom_du_fichier)[0])
    W_reshape = W.reshape(int(np.sqrt(W.shape[0])), int(np.sqrt(W.shape[0])))
    
    return W_reshape



if __name__ == "__main__":
    W = decode_reshape_W("parametres.txt")
    u.show(W)
