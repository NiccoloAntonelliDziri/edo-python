import numpy as np
import pylab as pl

class Field:
    def __init__(self):
        pass

    def plot(self, model, xaxis, yaxis, taxis):
        x = np.linspace(xaxis.get_start(), xaxis.get_end(), xaxis.get_nb_points_subdivision())
        y = np.linspace(yaxis.get_start(), yaxis.get_end(), yaxis.get_nb_points_subdivision())
        t = np.linspace(taxis.get_start(), taxis.get_end(), taxis.get_nb_points_subdivision())

        X, Y = np.meshgrid(x, y)

        Yarr = [X, Y]

        u, v = model.rhs(Yarr, t)
        
        return pl.quiver(X, Y, u, v)
