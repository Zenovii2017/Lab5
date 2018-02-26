# module that have class AcademicBuilding
# writed Zenovii Popenyuk
class AcademicBuilding():
    """
    class AcademicBuilding
    have parameter adress and classrooms
    have function:
        total_equimpent():
            return all equimpent in Acdemic Buiding
    """
    def __init__(self, adress='', classrooms = []):
        """
        parameter adress - str
                  classrooms - list
        announces variables
        """
        self.adress = adress
        self.classrooms = classrooms

    def total_equipment(self):
        """
        return lst
        calculate all equimpent in Academic Building
        """
        lst = []
        count_set = set()
        for room in self.classrooms:
            for equimpent in room.equimpent:
                lst.append(equimpent)
                count_set.add(equimpent)
        final_lst = []
        for only in count_set:
            final_lst.append((only, lst.count(only)))
        return final_lst


    def __str__(self):
        """
        return str
        its for print all about Academic Building
        """
        sentence = self.adress
        for i in self.classrooms:
            sentence +='\n' + str(i)
        return sentence
