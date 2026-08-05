from model.vehicle import Vehicle

class Van(Vehicle):

    def __init__(self):
        super().__init__()
        self.priceMultipliers = {
            # Standard
            "transmission": 1.20,
            "brake": 1.30,
            "alternator": 1.10,
            "muffler": 1.10,
            "chassis": 1.40,
            "struts": 1.30,
            "bonnet": 1.15,
            "engine": 1.35,
            "battery": 1.20,
            "axle": 1.35,
            "catalytic-converter": 1.10,
            "fuel-tank": 1.35,
            "cooling-system": 1.20,
            "electric-power-system": 1.15,
            "bumper": 1.20,
            "suspension": 1.35,
            "radiator": 1.20,
            "ignition": 1.10,
            "clutch": 1.20,
            "steering-system": 1.20,
            "rims": 1.25,
            "gearbox": 1.25,
            "differential": 1.35
        }