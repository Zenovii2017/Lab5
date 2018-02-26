def test_triangle():
    """
    test triangle and search count of errors
    :return: int
    """
    errors = 0
    try:
        import triangle
        import point
    except:
        errors += 1
    try:
        triangle = triangle.Triangle(point.Point(1, 1), point.Point(3, 1),\
                                     point.Point(2, 3))
    except:
        errors += 1
    try:
        print(triangle.is_triangle())
    except:
        errors += 1
    try:
        print(triangle.perimeter())
    except:
        errors += 1
    try:
        print(triangle.area())
    except:
        errors += 1
    try:
        print(triangle)
    except:
        errors += 1
    return errors

print('There are {} errors.'.format(test_triangle()))
