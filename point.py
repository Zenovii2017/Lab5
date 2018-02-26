# module that have class Point
# writed by Zenovii Popenyuk

class Point():
    """
    class Point
    have parameter x, y
    have function:
        lenght():
            return lenght between two point
    """
    def __init__(self, x=0, y=0):
        """
        announces variables
        """
        self.x = x
        self.y = y


    def lenght(self,another_self):
        """
        serch lenght between two point
        :param another_self: Point
        :return: float
        """
        import math
        len = math.sqrt((self.x - another_self.x) ** 2 + (self.y - \
                                                    another_self.y) ** 2)
        return len
