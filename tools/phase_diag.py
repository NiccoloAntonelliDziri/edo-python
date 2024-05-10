import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from .field import Field

class PhaseDiagram:
    def __init__(self, title = "Phase Diagram", figsize = (10, 6)):
        self.__title = title
        self.__figsize = figsize

    def get_title(self):
        return self.__title

    def get_figsize(self):
        return self.__figsize

    def set_title(self, newtitle):
        self.__title = newtitle

    def set_figsize(self, newfigsize):
        self.__figsize = newfigsize

    def portrait(self, model, xaxis, yaxis, taxis, initials, show_field = True, exportpng = False):
        # -- préparer le graphique
        fig, phases = plt.subplots(figsize = self.get_figsize())

        # -- paramétrages graphique globaux
        plt.xlim(xaxis.get_start(), xaxis.get_end())
        plt.ylim(yaxis.get_start(), yaxis.get_end())

        # -- paramétrages repère
        phases.grid(True)
        phases.set_title(self.get_title())
        phases.set_xlabel(xaxis.get_label())
        phases.set_ylabel(yaxis.get_label())

        # -- Calcul des trajectoires
        t = np.linspace(taxis.get_start(),
                        taxis.get_end(),
                        taxis.get_nb_points_subdivision())

        condi_init = initials.get_initials()
        for init in condi_init:
            y0 = init.get_coords()
            traj = odeint(model.get_rhs(), y0, t)
            phases.plot(traj[:, 0], traj[:, 1])

        # -- Champs de vecteurs
        if show_field:
            field = Field()
            field.plot(model, xaxis, yaxis)

        plt.show()

        if exportpng:
            figname = self.get_title().replace(" ", "_") + ".png"
            fig.savefig(figname)
