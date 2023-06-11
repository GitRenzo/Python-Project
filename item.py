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
        self.__name = name
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

    #GET
    #Propery decorator = read only attribute
    @property
    def name(self):
        #When you use the Getter the code here is executed
        #i.e: print(item1.name)
        return self.__name
    
    #SET
    #This allows to set a new name even though it was marked a read only attribute
    @name.setter
    def name(self, value):
        #When you use a setter the code here is executed
        #i.e. item1.name = "Value" (The value is the parameter passsed to this method)
        self.__name = value
        return self.__name
    # this magic method helps to represent in a human readable way the All list
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')" 
