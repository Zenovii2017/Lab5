def test():
    """
    Test
    :return: str
    """
    errors = 0
    try:
        from Task_4_Zenovii_Popenyuk import Property, Apartment, get_valid_input,\
        promt_init, House, Rental, Purchase, HouseRental, ApartmentRental,\
        ApartmentPurschase, HousePurschase, Agent
    except:
        errors += 1
    try:
        get_valid_input("what laundry? ", ("coin", "ensuite", "none"))
    except:
        errors += 1
    try:
        init = HouseRental().prompt_init()
        house = HouseRental(**init)
        house.display()
    except:
        errors += 1
    try:
        agent = Agent()
        agent.add_property()
        agent.display_properties()
        agent.print_property()
    except:
        errors += 1
    return 'There are {} errors'.format(errors)

print(test())