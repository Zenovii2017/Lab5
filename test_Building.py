def test_Building():
    """
    calcute count errors
    :return: int
    """
    errors = 0
    try:
        import Classroom as classroom
        import Building
    except:
        errors += 1
    try:
        classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector',\
                                                        'mic'])
        classroom_007 = classroom.Classroom('007', 12, ['TV'])
        classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        classrooms = [classroom_016, classroom_007, classroom_008]
        building = Building.AcademicBuilding('Kozelnytska st. 2a', classrooms)
    except:
        errors += 1
    try:
        print(building.adress)
    except:
        errors += 1
    try:
        for room in building.classrooms:
            print(room)
    except:
        errors += 1
    try:
        print(building.total_equipment())
    except:
        errors += 1
    try:
        print(building)
    except:
        errors += 1
    return errors

print('There are {} errors.'.format(test_Building()))
