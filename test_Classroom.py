def test_Classroom():
    """
    test class Classroom
    return count of errors
    :return: int
    """
    errors = 0
    try:
        import classroom
    except:
        errors += 1
    try:
        classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector',\
                                                        'mic'])
        classroom_007 = classroom.Classroom('007', 12, ['TV'])
    except:
        errors += 1
    try:
        classroom_016.number
        classroom_016.capacity
        classroom_016.equimpent
    except:
        errors += 1
    try:
        classroom_016.equipment_differences(classroom_007)
    except:
        errors += 1
    try:
        print(classroom_016)
    except:
        errors += 1
    try:
        [classroom_016]
    except:
        errors += 1
    return errors


print('There are {} errors.'.format(test_Classroom()))
