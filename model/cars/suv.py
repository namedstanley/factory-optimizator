from model.vehicle import Vehicle

class SUV(Vehicle):

    def __init__(self):
        super().__init__()
        self.priceMultipliers = {
            # Standard
            "transmission": 1.12,
            "brake": 1.18,
            "alternator": 1.00,
            "muffler": 1.05,
            "chassis": 1.30,
            "struts": 1.20,
            "bonnet": 1.10,
            "engine": 1.25,
            "battery": 1.05,
            "axle": 1.25,
            "catalytic-converter": 1.05,
            "fuel-tank": 1.20,
            "cooling-system": 1.10,
            "electric-power-system": 1.05,
            "bumper": 1.15,
            "suspension": 1.25,
            "radiator": 1.10,
            "ignition": 1.00,
            "clutch": 1.10,
            "steering-system": 1.15,
            "rims": 1.15,
            "gearbox": 1.15,
            "differential": 1.25,

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