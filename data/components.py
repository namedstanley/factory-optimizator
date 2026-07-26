from model.component import Component
import random

def retrieveStandardComponents():
    return {
        "transmission": Component(id=random.randint(1000,9999), name="transmission", price=random.randint(2200,3200), assembly_time=random.randint(6,9)),
        "brake": Component(id=random.randint(1000,9999), name="brake", price=random.randint(500,900), assembly_time=random.randint(2,4)),
        "alternator": Component(id=random.randint(1000,9999), name="alternator", price=random.randint(250,450), assembly_time=random.randint(1,2)),
        "muffler": Component(id=random.randint(1000,9999), name="muffler", price=random.randint(350,700), assembly_time=random.randint(1,3)),
        "chassis": Component(id=random.randint(1000,9999), name="chassis", price=random.randint(4000,6500), assembly_time=random.randint(10,15)),
        "struts": Component(id=random.randint(1000,9999), name="struts", price=random.randint(400,700), assembly_time=random.randint(2,4)),
        "bonnet": Component(id=random.randint(1000,9999), name="bonnet", price=random.randint(500,900), assembly_time=random.randint(2,4)),
        "engine": Component(id=random.randint(1000,9999), name="engine", price=random.randint(6000,9500), assembly_time=random.randint(12,18)),
        "battery": Component(id=random.randint(1000,9999), name="battery", price=random.randint(250,600), assembly_time=random.randint(1,3)),
        "axle": Component(id=random.randint(1000,9999), name="axle", price=random.randint(700,1200), assembly_time=random.randint(3,5)),
        "catalytic-converter": Component(id=random.randint(1000,9999), name="catalytic-converter", price=random.randint(900,1700), assembly_time=random.randint(3,5)),
        "fuel-tank": Component(id=random.randint(1000,9999), name="fuel-tank", price=random.randint(450,800), assembly_time=random.randint(2,4)),
        "cooling-system": Component(id=random.randint(1000,9999), name="cooling-system", price=random.randint(700,1200), assembly_time=random.randint(3,5)),
        "electric-power-system": Component(id=random.randint(1000,9999), name="electric-power-system", price=random.randint(1200,2200), assembly_time=random.randint(4,6)),
        "bumper": Component(id=random.randint(1000,9999), name="bumper", price=random.randint(350,700), assembly_time=random.randint(1,3)),
        "suspension": Component(id=random.randint(1000,9999), name="suspension", price=random.randint(1200,2200), assembly_time=random.randint(4,6)),
        "radiator": Component(id=random.randint(1000,9999), name="radiator", price=random.randint(350,700), assembly_time=random.randint(2,3)),
        "ignition": Component(id=random.randint(1000,9999), name="ignition", price=random.randint(250,500), assembly_time=random.randint(1,2)),
        "clutch": Component(id=random.randint(1000,9999), name="clutch", price=random.randint(600,1100), assembly_time=random.randint(2,4)),
        "steering-system": Component(id=random.randint(1000,9999), name="steering-system", price=random.randint(900,1700), assembly_time=random.randint(3,5)),
        "rims": Component(id=random.randint(1000,9999), name="rims", price=random.randint(700,1400), assembly_time=random.randint(2,4)),
        "gearbox": Component(id=random.randint(1000,9999), name="gearbox", price=random.randint(1800,3200), assembly_time=random.randint(6,9)),
        "differential": Component(id=random.randint(1000,9999), name="differential", price=random.randint(1200,2200), assembly_time=random.randint(4,6)),
    }

def retrievePremiumComponents():
    return {
        "leather-seats": Component(id=random.randint(1000,9999), name="leather-seats", price=random.randint(1800,3200), assembly_time=random.randint(4,7)),
        "digital-dashboard": Component(id=random.randint(1000,9999), name="digital-dashboard", price=random.randint(1400,2600), assembly_time=random.randint(3,5)),
        "head-up-display": Component(id=random.randint(1000,9999), name="head-up-display", price=random.randint(900,1800), assembly_time=random.randint(2,4)),
        "adaptive-cruise-control": Component(id=random.randint(1000,9999), name="adaptive-cruise-control", price=random.randint(1600,3000), assembly_time=random.randint(4,6)),
        "lane-assist-system": Component(id=random.randint(1000,9999), name="lane-assist-system", price=random.randint(1200,2200), assembly_time=random.randint(3,5)),
        "panoramic-roof": Component(id=random.randint(1000,9999), name="panoramic-roof", price=random.randint(2200,4200), assembly_time=random.randint(6,10)),
        "premium-audio-system": Component(id=random.randint(1000,9999), name="premium-audio-system", price=random.randint(1400,2600), assembly_time=random.randint(3,5)),
        "ambient-lighting": Component(id=random.randint(1000,9999), name="ambient-lighting", price=random.randint(300,800), assembly_time=random.randint(1,2)),
        "heated-seats": Component(id=random.randint(1000,9999), name="heated-seats", price=random.randint(700,1200), assembly_time=random.randint(2,3)),
        "ventilated-seats": Component(id=random.randint(1000,9999), name="ventilated-seats", price=random.randint(900,1700), assembly_time=random.randint(2,4)),
        "wireless-charger": Component(id=random.randint(1000,9999), name="wireless-charger", price=random.randint(150,450), assembly_time=random.randint(1,2)),
        "surround-camera-system": Component(id=random.randint(1000,9999), name="surround-camera-system", price=random.randint(1400,2600), assembly_time=random.randint(3,5)),
    }

def retrieveTuningComponents():
    return {
        "sport-exhaust": Component(id=random.randint(1000,9999), name="sport-exhaust", price=random.randint(1500,3200), assembly_time=random.randint(3,5)),
        "turbocharger-kit": Component(id=random.randint(1000,9999), name="turbocharger-kit", price=random.randint(3800,7000), assembly_time=random.randint(7,11)),
        "performance-air-intake": Component(id=random.randint(1000,9999), name="performance-air-intake", price=random.randint(500,1100), assembly_time=random.randint(1,2)),
        "coilover-suspension": Component(id=random.randint(1000,9999), name="coilover-suspension", price=random.randint(1800,3500), assembly_time=random.randint(4,6)),
        "big-brake-kit": Component(id=random.randint(1000,9999), name="big-brake-kit", price=random.randint(2200,4200), assembly_time=random.randint(4,6)),
        "carbon-fiber-hood": Component(id=random.randint(1000,9999), name="carbon-fiber-hood", price=random.randint(1800,3500), assembly_time=random.randint(3,5)),
        "rear-spoiler": Component(id=random.randint(1000,9999), name="rear-spoiler", price=random.randint(400,1200), assembly_time=random.randint(1,2)),
        "side-skirts": Component(id=random.randint(1000,9999), name="side-skirts", price=random.randint(300,900), assembly_time=random.randint(1,2)),
        "sport-rims": Component(id=random.randint(1000,9999), name="sport-rims", price=random.randint(1400,2800), assembly_time=random.randint(2,4)),
        "low-profile-tires": Component(id=random.randint(1000,9999), name="low-profile-tires", price=random.randint(900,1800), assembly_time=random.randint(2,3)),
        "ecu-remap": Component(id=random.randint(1000,9999), name="ecu-remap", price=random.randint(600,1400), assembly_time=random.randint(1,2)),
        "sport-steering-wheel": Component(id=random.randint(1000,9999), name="sport-steering-wheel", price=random.randint(400,1000), assembly_time=random.randint(1,2)),
    }