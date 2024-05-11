class Initial:
    def __init__(self, x, y, color = 'blue', linestyle = 'solid'):
        self._x = x
        self._y = y
        self._color = color
        self._linestyle = linestyle

    def get_coords(self):
        return [self._x, self._y]

    def get_color(self):
        return self._color

    def get_linestyle(self):
        return self._linestyle

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_color(self, color):
        self._color = color

    def set_linestyle(self, linestyle):
        self._linestyle = linestyle

"""
Conteneur pour les conditions initiales

C'est un itérable qui contient des objets Initial
"""
class Initials:
    def __init__(self, initials = list()):
        self._initials = initials
        self._nb_initials = len(initials)

    def __iter__(self):
        return iter(self._initials)

    def __next__(self):
        self.i = 0
        if self.i < self._nb_initials:
            self.i += 1
            return self._initials[self.i]
        else:
            raise StopIteration

    def get_initials(self):
        return self._initials

    # No error handling
    def append(self, x, y, color = 'blue', linestyle = 'solid'):
        self._initials.append(Initial(x, y, color, linestyle))
        self._nb_initials += 1

    # No error handling
    def pop_initial(self):
        self._initials.pop()
        self._nb_initials -= 1

    def clear_initials(self):
        self._initials.clear()
        self._nb_initials = 0

