# module that have class Triangle
# writed by Zenovii Popenyuk


class Triangle():
    """
    class Triangle
    have parameter point_A, point_B, point_C
    have function:
        is_triangle():
            return true if this triangle can exist else false
        perimeter():
            return perimer of triangle
        area():
            return areo of triangle
    """

    def __init__(self, point_A, point_B, point_C):
        """
        announces variables
        """
        self.len_a = point_A.lenght(point_B)
        self.len_b = point_B.lenght(point_C)
        self.len_c = point_C.lenght(point_A)

    def __str__(self):
        """
        its for print user
        :return: str
        """
        return 'Three lenght of side : {}, {}, {}'.format(self.len_a,\
                                                          self.len_b,\
                                                          self.len_c)

    def __repr__(self):
        """
        its for ptint of programist
        :return: str
        """
        return self.len_a, self.len_b, self.len_c

    def is_triangle(self):
        """
        calculate if this triangle can exist
        :return: bool
        """
        len1 = self.len_a
        len2 = self.len_b
        len3 = self.len_c
        if len1 >= len2 + len3 or len2 >= len1 + len3 or len3 >= len1 + len2:
            return False
        return True

    def perimeter(self):
        """
        return perimeter of triangle
        :return: float
        """
        return self.len_a + self.len_b + self.len_c

    def area(self):
        """
        return area of triangle
        :return: float
        """
        import math
        a = self.len_a
        b = self.len_b
        c = self.len_c
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
