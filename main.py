class Item:
    # Magic methods which start with double underscore _ _

    # this magic method init is executed everytime the class is instantiated, the SELF value is the object itself and any other values
    # are asummed to be mandatory or it will be an error when you try to execute the code
    # name, price and quantity are mandatory paramenters
    # the mandatory parameters can have default values as quantity in this example, so you dont have to pass it
    def __init__(self, name: str, price: float, quantity=0):

        # Run validations to the received arguments
        assert price >= 0, f"The value {price} is not greater or equal to 0"
        assert quantity >= 0, f"The value {quantity} is not greater or equal to 0"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity= quantity
    def calculate_total_price(self):
        # this works because when you create an instance of an object like item1 and item2, the object sends itself as SELF argument
        # and the instance has a name, price and quantity
        return self.price * self.quantity

# This action is equivalent to create an instance of a class (item1 and item2 are objects)
item1 = Item("iPhone", 400, 2)
item2 = Item("Nokia", 240, 2)
# You can assign more attributes to the constructor
item2.has_keypad = False

print(item1.calculate_total_price())



# key concepts to study
# class vs object
# What is an instance and what is its relation with an object?
# Constructor
# Classes
# object
# Method vs function
# Attributes
