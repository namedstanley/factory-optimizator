from model.vehicle import Vehicle

class Hatchback(Vehicle):

    def __init__(self):
        super().__init__()
        self.priceMultipliers = {
            # Standard
            "transmission": 0.95,
            "brake": 0.90,
            "alternator": 0.95,
            "muffler": 0.90,
            "chassis": 0.85,
            "struts": 0.90,
            "bonnet": 0.90,
            "engine": 0.85,
            "battery": 0.90,
            "axle": 0.90,
            "catalytic-converter": 0.95,
            "fuel-tank": 0.85,
            "cooling-system": 0.90,
            "electric-power-system": 0.95,
            "bumper": 0.90,
            "suspension": 0.90,
            "radiator": 0.90,
            "ignition": 0.95,
            "clutch": 0.90,
            "steering-system": 0.95,
            "rims": 0.85,
            "gearbox": 0.90,
            "differential": 0.90,

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