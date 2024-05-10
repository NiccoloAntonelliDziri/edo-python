class Axis:
    def __init__(self, start, end, nb_points, label):
        self.__start = start
        self.__end = end
        self.__nb_points_subdivision = nb_points
        self.__label = label

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_nb_points_subdivision(self):
        return self.__nb_points_subdivision

    def get_label(self):
        return self.__label

    def set_label(self, newlabel):
        self.__label = newlabel

    def set_nb_points_subdivision(self, new_subdivision):
        self.__nb_points_subdivision = new_subdivision

    def set_end(self, end):
        self.__end = end

    def set_start(self, start):
        self.__start = start
        
