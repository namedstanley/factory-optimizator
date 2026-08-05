from model.vehicle import Vehicle

class Convertible(Vehicle):

    def __init__(self):
        super().__init__()
        self.priceMultipliers = {
            # Standard
            "transmission": 1.05,
            "brake": 1.10,
            "alternator": 1.00,
            "muffler": 1.05,
            "chassis": 1.15,
            "struts": 1.15,
            "bonnet": 1.10,
            "engine": 1.10,
            "battery": 1.00,
            "axle": 1.10,
            "catalytic-converter": 1.05,
            "fuel-tank": 1.00,
            "cooling-system": 1.05,
            "electric-power-system": 1.05,
            "bumper": 1.10,
            "suspension": 1.15,
            "radiator": 1.05,
            "ignition": 1.00,
            "clutch": 1.10,
            "steering-system": 1.10,
            "rims": 1.15,
            "gearbox": 1.10,
            "differential": 1.10,

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