from .models import AutonomSys

"""
x' = x * (a - b * x) - c*x*y / (m*y + x)
y' =  -d*y + f*x*y / (m*y + x)

"""
class AGKB(AutonomSys):
    def __init__(self, a, b, c, d, f, m):
        super().__init__("Arditi-Ginzburg ratio-dependent functional response")
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__f = f
        self.__m = m

    def rhs(self, y_vector, t):
        a = self.__a
        b = self.__b
        c = self.__c
        d = self.__d
        f = self.__f
        m = self.__m

        x = y_vector[0]
        y = y_vector[1]

        dxdt = x*(a - b*x) - c*x*y / (m*y + x)
        dydt = -d*y + f*x*y / (m*y + x)

        # Mettre condition pour que x et y restent positifs
        # quand les dérivées s'annulent

        return [dxdt, dydt]
