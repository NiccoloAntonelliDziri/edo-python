class AutonomSys:
    def __init__(self, name = ""):
        self._name = name

    def get_model_name(self):
        return self._name

    def set_model_name(self, newname):
        self._name = newname

    def get_rhs(self):
        return self.rhs

    """
    Retourne une liste de taille = dimensions du système
    """
    def rhs(self, x, y):
        return []
