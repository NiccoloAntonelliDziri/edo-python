from .models import AutonomSys

"""
x' = x * (alpha - beta * y)
y' = y * (delta * x - gamma)

-> réecriture des paramètres

x' = x * ( Kappa - y)
y' = y * ( x - Eps )

avec    Kappa = alpha / beta
et      Eps = gamma / delta
"""
class LotkaVolterra(AutonomSys):
    def __init__(self, kappa, eps):
        super().__init__("Lotka-Volterra")
        self.__kappa = kappa
        self.__eps = eps

    def get_kappa(self):
        return self.__kappa

    def get_eps(self):
        return self.__eps

    def set_kappa(self, newkappa):
        self.__kappa = newkappa

    def set_eps(self, neweps):
        self.__eps = neweps
    
    """
    t est utilisé uniquement dans le cas ou c'est le système est non autonome
    sinon le paramètre n'est pas utilisé
    """
    def rhs(self, y_vector, t):
        kappa = self.get_kappa()
        eps = self.get_eps()

        x, y = self.vector_to_xy(y_vector)

        dxdt = x * (kappa - y )
        dydt = y * ( x - eps)

        # Temporaire pour avoir la meme fonction que dans le tp
        dxdt = x * (( x - eps ) * (1. - (1./ kappa ) * x ) / ( x + eps ) - y )
        dydt = y * ( x - 1)

        return [dxdt, dydt]

