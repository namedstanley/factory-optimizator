from model.vehicle import Vehicle

class Coupe(Vehicle):

    def __init__(self):
        super().__init__()
        self.priceMultipliers = {
            # Standard
            "transmission": 1.10,
            "brake": 1.20,
            "alternator": 1.00,
            "muffler": 1.10,
            "chassis": 1.10,
            "struts": 1.15,
            "bonnet": 1.15,
            "engine": 1.20,
            "battery": 1.00,
            "axle": 1.15,
            "catalytic-converter": 1.05,
            "fuel-tank": 0.95,
            "cooling-system": 1.10,
            "electric-power-system": 1.05,
            "bumper": 1.10,
            "suspension": 1.20,
            "radiator": 1.10,
            "ignition": 1.00,
            "clutch": 1.15,
            "steering-system": 1.15,
            "rims": 1.20,
            "gearbox": 1.15,
            "differential": 1.20,

            # Premium
            "leather-seats": 1.00,
            "digital-dashboard": 1.00,
            "head-up-display": 1.00,
            "adaptive-cruise-control": 1.00,
            "lane-assist-system": 1.00,
            "panoramic-roof": 1.00,
            "premium-audio-system": 1.00,
            "ambient-lighting": 1.00,
            "heated-seats": 1.00,
            "ventilated-seats": 1.00,
            "wireless-charger": 1.00,
            "surround-camera-system": 1.00,

            # Tuning
            "sport-exhaust": 1.00,
            "turbocharger-kit": 1.00,
            "performance-air-intake": 1.00,
            "coilover-suspension": 1.00,
            "big-brake-kit": 1.00,
            "carbon-fiber-hood": 1.00,
            "rear-spoiler": 1.00,
            "side-skirts": 1.00,
            "sport-rims": 1.00,
            "low-profile-tires": 1.00,
            "ecu-remap": 1.00,
            "sport-steering-wheel": 1.00
        }