from item import Item

class Phone(Item):
    # The init from here calls the init from the parent, and the all list executes as well so it is not necessary to
    # create the all list here
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # |The super allows to access all the attributes from the parent
        super().__init__(name, price, quantity)
        assert broken_phones >=0, f"The value of {broken_phones} is not greater than zero"

        self.broken_phones = broken_phones
