class Vehicle:
    def __init__(self, type_of_vehicle, type_of_model, given_price):
        self.type = type_of_vehicle
        self.type_of_model = type_of_model
        self.given_price = given_price
        self.owner = None

    def __repr__(self):
        if self.owner is not None:
            return f'{self.type_of_model} {self.type} is owned by: {self.owner}'
        else:
            return f'{self.type_of_model} {self.type} is on sale: {self.given_price}'

    def buy(self, money, owner):
        if money >= self.given_price and self.owner is None:
            self.owner = owner
            return f'Successfully bought a {self.type}. Change: {money - self.given_price:.2f}'

        elif money >= self.given_price and self.owner is not None:
            return f'Car already sold'

        elif money < self.given_price:
            return f'Sorry, not enough money'

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return f'Vehicle has no owner'


