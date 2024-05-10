class Initial:
    def __init__(self, coords):
        self._coords = coords

    """
    Renvoie un tuple contenant les conditions initiales
    """
    def get_coords(self):
        return self._coords

    def set_cond_init(self, coords):
        self._coords = coords

"""
Conteneur pour les conditions initiales
"""
class Initials:
    def __init__(self, initials = list()):
        self._initials = initials

    def get_initials(self):
        return self._initials

    def append_initial(self, initial):
        self._initials.append(initial)

    def pop_initial(self):
        self._initials.pop()

    def clear_initials(self):
        self._initials.clear()

