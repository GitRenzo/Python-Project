import csv

class Item:
    #To have all the instances in a list
    all = []
    # class attributes
    pay_rate = 0.8 #class attribute for the pay rate

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

        #The init is executed everytime an instance is created, this way we can add each item to the list
        Item.all.append(self)
    def calculate_total_price(self):
        # this works because when you create an instance of an object like item1 and item2, the object sends itself as SELF argument
        # and the instance has a name, price and quantity
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity')),
                )
    
    @staticmethod
    def is_intenger(num):
        #We will count out the floats that are point zero 
        #For i.e 5.0, 10.0
        if isinstance(num, float):
            return  num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False            

    # this magic method helps to represent in a human readable way the All list
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')" 

#INHERITANCE
#The class Phone inherits from Item
class Phone(Item):
    # The init from here calls the init from the parent, and the all list executes as well so it is not necessary to
    # create the all list here
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # |The super allows to access all the attributes from the parent
        super().__init__(name, price, quantity)
        assert broken_phones >=0, f"The value of {broken_phones} is not greater than zero"

        self.broken_phones = broken_phones

# This action is equivalent to create an instance of a class (item1 and item2 are objects)
# item1 = Item("iPhone", 400, 2)
# item2 = Item("Nokia", 100, 2)
# You can assign more attributes to the constructor
# item2.has_keypad = False
# item2.apply_discount()
# print(item2.price) show the price after the discount is applied to the product

# print(item1.calculate_total_price())


# print(Item.__dict__) # Returns all the class attributes
# print(item1.__dict__) # Returns all the instance attributes


# You can assign the value of the class attribute for the object
# item3 = Item('Samsung', 100, 1)
# item3.pay_rate = 0.6
# item3.apply_discount()
# print(item3.price)
# item4 = Item('Dell', 100, 2)
# item5 = Item('Sony', 120, 2)

# This way we can access al the instnaces created, which are saved in the All list
# for instance in Item.all:
#     print(instance.name)

# __repr__ magic method results
# print(Item.all)

# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_intenger(2))

# To test INHERITANCE
phone1 = Phone("iPhone", 700, 2, 1)
print(phone1.calculate_total_price())


# key concepts to study
# Class attributes vs instance attributes
# What is a class method
# what is a static method
# class method vs static method
# Inheritance, parent class and child classes 
# The super function in inheritance