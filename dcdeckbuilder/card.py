class Card:
    def __init__(self, name: str, power: int, cost: int, cardtype:str):
        self.name = name
        self.power = power
        self.cost = cost
        self.cardtype = cardtype
    
    def increase_power(self, power:str):
        self.power += power

    def decrease_power(self, power:str):
        self.power -= power 