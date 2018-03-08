class Property:
    """
    class Property
    have functions:
        display -
        promt_init - return dict
    """
    def init(self, square_feet='', beds='', baths='', **kwargs):
        """
        initialisate class
        :param square_feet: str
        :param beds: str
        :param baths: str
        """
        super().init(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        print property details and all date of this property
        :return: None
        """
        print("PROPERTY DETAILS")
        print('================')
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def promt_init():
        """
        make a dict with key square_feet, beds and baths
        :return: dict
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input('Enter number of bedrooms: '),
                    baths=input('Enter number of baths: '))

    promt_init = staticmethod(promt_init)


class Apartment(Property):
    """
    Class Apartment
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def init(self, balcony='', laundry='', **kwargs):
        """
        initialise class
        :param balcony: str
        :param laundry: str
        :param kwargs: str
        :return: None
        """
        super().init(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        print data about apartment
        :return: None
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: &s" % self.laundry)
        print("balconies: &s" % self.laundry)

    def promt_init():
        """
        add to dict of property new date about laudry and balcony
        :return: dict
        """
        parent_init = Property.promt_init()
        laundry = get_valid_input("What laundry facilities does "
                                  "the property has?",
                                  Apartment.valid_laundries)

        balcony = get_valid_input("Does property have balcony ?",
                                  Apartment.valid_balconies)

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    promt_init = staticmethod(promt_init)


def get_valid_input(input_string, valid_options):
    """
    make new sentence to date
    :param input_string: str
    :param valid_options: str
    :return: str
    """
    input_string += " ({}) ". format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


def promt_init():
    """
    add new date to property dict
    :return: dict
    """
    parent_init = Property.promt_init()
    laundry = get_valid_input(
            'what laudry facilities does'
            'the property have?',
            Apartment.valid_laundries)
    balcony = get_valid_input(
        "Docs the property have a balcony? ",
        Apartment.valid_balconies)
    parent_init.update(
        {"laundry": laundry,
         "balcony": balcony})
    return parent_init
promt_init = staticmethod(promt_init)


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def init(self, num_stories='', garage='', fenced='', **kwargs):
        """
        initialise class House
        :param num_stories: str
        :param garage: str
        :param fenced: str
        :param kwargs: all that remains
        :return: None
        """
        super().init(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def desplay(self):
        """
        print House details
        :return: None
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories".format(self.num_stories))
        print("Garage: {}".format(self.garage))
        print("Fenced yard: {}".format(self.fenced))

    def promt_init():
        """
        add new date to property dict about fenced garage and num_stories
        :return: dict
        """
        parent_init = Property.promt_init()
        fenced = get_valid_input('Is the yard fenced?', House.valid_fenced)
        garage = get_valid_input('Is there a garage?', House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    promt_init = staticmethod(promt_init)


class Purchase():
    def init(self, price='', taxes='', **kwargs):
        """
        initialise class init
        :param price: str
        :param taxes: str
        :param kwargs: all that remains
        :return: None
        """
        super().init(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Print all date about Purchase details
        :return: None
        """
        super().display()
        print('PURCHASE DETAILS')
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def promt_init():
        """
        make a dictwuth key price and taxes
        :return: dict
        """
        return dict(
            price=input("WHat is the selling price? "),
            taxes=input("What are the estimated taxes? "))
    promt_init = staticmethod(promt_init)


class Rental:
    def __init__(self, furnished='', utilities='',
                rent='', **kwargs):
        """
        initialise class Rental
        :param furnished: str
        :param utilities: str
        :param rent: str
        :param kwargs: all that remains
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        print rental data
        :return: None
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        make dict with key rent utilities
        :return: dict
        """
        return dict(
            rent=input("What is the mountly rent? "),
            utilities=input(
                "What are the estimated utilities?"),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))
    promt_init = staticmethod(promt_init)


class HouseRental():
    def promt_init():
        """
        update class house with rental
        :return: dict
        """
        init = House.promt_init()
        rental = Rental().promt_init()
        init.update(rental)
        return init
    promt_init = staticmethod(promt_init)


class ApartmentRental():
    def promt_init():
        """
        update class Apartment with rental
        :return:  dict
        """
        init = Apartment.promt_init()
        rental = Rental().promt_init()
        init.update(rental)
        return init
    promt_init = staticmethod(promt_init)


class ApartmentPurschase():
    def promt_init():
        """
        update apartmant class with purchase
        :return: dict
        """
        init = Apartment.promt_init()
        purchase = Purchase().promt_init()
        init.update(purchase)
        return init
    promt_init = staticmethod(promt_init)


class HousePurschase():
    def promt_init():
        """
        update class house with purchase
        :return: dict
        """
        init = House().promt_init()
        purchase = Purchase.promt_init()
        init.update(purchase)
        return init
    promt_init = staticmethod(promt_init)


class Agent:
    def __init__(self):
        """
        initialise class Agent
        """
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurschase,
        ("apartment", "rental"): ApartmentPurschase
        }

    def add_property(self):
        """
        add property to exist property
        :return: None
        """
        property_type = get_valid_input(
            "What type of property",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? "
            ("purchase", "rental")).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.promt_init()
        self.property_list.append(PropertyClass(**init_args))

    def print_property(self):
        """
        print property and type_map
        :return:
        """
        for property in self.property_list:
            print(property)
        for key in self.type_map:
            print(key, " : ", self.type_map)

    def list_properties(self, show_all=False):
        """
        if indentificator == true print property else return them
        :param show_all:
        :return:
        """
        if show_all is True:
            self.print_property()
        else:
            return self.property
