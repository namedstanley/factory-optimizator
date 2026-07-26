from model.component import Component

class Vehicle:

    def __init__(self):
        self.vin = ""
        self.hp = 0
        self.capacity = 0.0
        self.fuel = ""

        self.standardComponents: dict[str, Component] = {}
        self.premiumComponents: dict[str, Component] = {}
        self.tuningComponents: dict[str, Component] = {}

        self.productionTime = 0.0
        self.productionPrice = 0.0

        self.isPremium = False
        self.isTuned = False