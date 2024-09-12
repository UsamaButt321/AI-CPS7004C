class Location:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"location is {self.__x}, {self.__y}"

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def equals(self, location):
        if isinstance(location, Location):
            return (self.__x == location.get_x() and
                    self.__y == location.get_y())
        return False