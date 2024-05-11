from .models import AutonomSys

"""
Arditi-Ginzburg ratio-dependent functional response

Kuang-Beretta Model:

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

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_f(self):
        return self.__f

    def get_m(self):
        return self.__m

    def set_a(self, newa):
        self.__a = newa

    def set_b(self, newb):
        self.__b = newb

    def set_c(self, newc):
        self.__c = newc

    def set_d(self, newd):
        self.__d = newd

    def set_f(self, newf):
        self.__f = newf

    def set_m(self, newm):
        self.__m = newm

    def rhs(self, y_vector, t):
        a = self.__a
        b = self.__b
        c = self.__c
        d = self.__d
        f = self.__f
        m = self.__m

        x, y = self.vector_to_xy(y_vector)
                
        dxdt = x*(a - b*x) - c*x*y / (m*y + x)
        dydt = -d*y + f*x*y / (m*y + x)

        # Mettre condition pour que x et y restent positifs
        # quand les dérivées s'annulent

        return [dxdt, dydt]

    #----------------------------
    # Calcul des points critiques
    
    def pt_0(self):
        return [0,0]

    def pt_1(self):
        a = self.get_a()
        b = self.get_b()
        return [a/b, 0]

    def pt_2(self):
        a = self.get_a()
        b = self.get_b()
        c = self.get_c()
        d = self.get_d()
        f = self.get_f()
        m = self.get_m()
        
        x = (c*d + f*(a*m - c))/(b*m*f)
        y = x * ((f - d)/(d*m))

        return [x, y]

    def get_list_pts_critiques(self):
        return [self._pt_0(), self._pt_1(), self._pt_2()]
