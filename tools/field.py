import numpy as np
import pylab as pl

class Field:
    def __init__(self, color = 'green', normalized_arrows = False):
        self.__color = color
        self.__normalized_arrows = normalized_arrows

    def get_color(self):
        return self.__color

    def set_color(self, newcolor):
        self.__color = newcolor

    def toggle_normalized_arrows(self):
        self.__normalized_arrows = not self.__normalized_arrows
    
    """
    Normalise un vecteur pour avoir une longueur de 1.

    u et v sont les composantes du vecteur
    """
    def _normalize_arrow(self, u, v):
        vector = np.array([u, v])
        norm = np.linalg.norm(vector)
        if norm == 0: 
            return 0
        return vector / norm

    def plot(self, model, xaxis, yaxis, taxis):
        x = np.linspace(xaxis.get_start(), xaxis.get_end(), xaxis.get_nb_points_subdivision())
        y = np.linspace(yaxis.get_start(), yaxis.get_end(), yaxis.get_nb_points_subdivision())
        t = np.linspace(taxis.get_start(), taxis.get_end(), taxis.get_nb_points_subdivision())

        X, Y = np.meshgrid(x, y)

        Yarr = [X, Y]

        u, v = model.rhs(Yarr, t)

        col = self.get_color()

        if self.__normalized_arrows:
            for i in range(len(u)):
                for j in range(len(u[i])):
                    u[i][j], v[i][j] = self._normalize_arrow(u[i][j], v[i][j])
        
        return pl.quiver(X, Y, u, v, color = col)
