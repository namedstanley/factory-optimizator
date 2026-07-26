from model.vehicle import Vehicle
from model.cars.convertible import *
from model.cars.coupe import *
from model.cars.hatchback import *
from model.cars.sedan import *
from model.cars.suv import *
from model.cars.van import *
from data.multipliers import *
from data.components import *
import random
import string

class ProcessHandler:

    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ProcessHandler,cls).__new__(cls)
        return cls.__instance
    
    def __init__(self):
        self.__designer = self.Designer()
        self.__assembler = self.Assembler()
        self.__vehicles = []

    def createVehicle(self, vehicle: Vehicle):

        match vehicle:
            case SUV():
                multiplier = SUV_PRICE_MULTIPLIERS

            case Sedan():
                multiplier = SEDAN_PRICE_MULTIPLIERS

            case Hatchback():
                multiplier = HATCHBACK_PRICE_MULTIPLIERS

            case Convertible():
                multiplier = CONVERTIBLE_PRICE_MULTIPLIERS

            case Van():
                multiplier = VAN_PRICE_MULTIPLIERS

            case Coupe():
                multiplier = COUPE_PRICE_MULTIPLIERS

            case _:
                raise Exception("Vehicle not supported")

        standardComponents, premiumComponents, tuningComponents = self.__designer.designVehicleComponents(multiplier)

        vehicle = self.__assembler.assemble_vehicle(
            vehicle,
            standardComponents,
            premiumComponents if vehicle.isPremium else {},
            tuningComponents if vehicle.isTuned else {}
        )

        self.__vehicles.append(vehicle)

        return vehicle

    class Designer:

        def __init__(self):
            self.__standardComponents = {}
            self.__premiumComponents = {}
            self.__tuningComponents = {}
        
        def __initStandardComponents(self):
            self.__standardComponents = retrieveStandardComponents()

        def __initPremiumComponents(self):
            self.__premiumComponents = retrievePremiumComponents()

        def __initTuningComponents(self):
            self.__tuningComponents = retrieveTuningComponents()

        def designVehicleComponents(self, multiplier: dict) -> dict:
            self.__initStandardComponents()
            self.__initPremiumComponents()
            self.__initTuningComponents()

            standardComponents = {}
            for k, v in self.__standardComponents.items():
                standardComponents[k] = v
                standardComponents[k].price = float(v.price * multiplier.get(k, 1.0))
            premiumComponents = {}
            for k, v in self.__premiumComponents.items():
                premiumComponents[k] = v
                premiumComponents[k].price = float(v.price * multiplier.get(k, 1.0))
            tuningComponents = {}
            for k, v in self.__tuningComponents.items():
                tuningComponents[k] = v
                tuningComponents[k].price = float(v.price * multiplier.get(k, 1.0))
            
            return ( standardComponents, premiumComponents, tuningComponents )

    class Assembler:

        def __init__(self):
            pass

        def assemble_vehicle(self, vehicle: Vehicle, standardComponents: dict, premiumComponents: dict, tuningComponents: dict) -> Vehicle:
            
            vehicle.standardComponents = standardComponents
            vehicle.premiumComponents = premiumComponents
            vehicle.tuningComponents = tuningComponents
            
            vehicle.vin = "".join([string.ascii_uppercase[random.randint(0,len(string.ascii_uppercase)-1)] if i%2 == 0 else str(random.randint(0,10)) for i in range(8)])
            vehicle.hp = random.randint(80,200)
            vehicle.capacity = random.randint(10,25)/10
            vehicle.fuel = "gasoline" if (random.randint(1,2) % 2) == 0 else "diesel"
            
            standardComponentsPrice = premiumComponentsPrice = tuningComponentsPrice = 0.0
            standardComponentsTime = premiumComponentsTime = tuningComponentsTime = 0.0
            
            for component in vehicle.standardComponents.values():
                #print("Assembling standard component " + component.name + " is going to take " + str(component.assembly_time) + " hours")
                #print(component.name + " assembled")
                standardComponentsPrice += component.price
                standardComponentsTime += component.assembly_time
            #print("Assembling standard components took " + str(standardComponentsTime) + " days and " + str(standardComponentsPrice) + "$ for " + vehicle.vin)

            for component in vehicle.premiumComponents.values():
                #print("Assembling premium component " + component.name + " is going to take " + str(component.assembly_time) + " hours")
                #print(component.name + " assembled")
                premiumComponentsPrice += component.price
                premiumComponentsTime += component.assembly_time
            #print("Assembling premium components took " + str(premiumComponentsTime) + " days and " + str(premiumComponentsPrice) + "$ for " + vehicle.vin)

            for component in vehicle.tuningComponents.values():
                #print("Assembling tuning component " + component.name + " is going to take " + str(component.assembly_time) + " hours")
                #print(component.name + " assembled")
                tuningComponentsPrice += component.price
                tuningComponentsTime += component.assembly_time
            #print("Assembling tuning components took " + str(tuningComponentsTime) + " days and " + str(tuningComponentsPrice) + "$ for " + vehicle.vin)
            
            vehicle.productionPrice = round(standardComponentsPrice + premiumComponentsPrice + tuningComponentsPrice, 2)
            vehicle.productionTime = round(standardComponentsTime + premiumComponentsTime + tuningComponentsTime, 2)

            #print("Total production time: " + str(vehicle.productionTime))
            #print("Total price: " + str(vehicle.productionPrice) + "$")
            return vehicle

    class ProductionPlanner:

        def __init__(self):
            self.__productionLot = {}

        def generateProductionLot(self):

            self.__productionLot = {
                SUV: random.randint(2, 10),
                Coupe: random.randint(2, 10),
                Sedan: random.randint(2, 10),
                Hatchback: random.randint(2, 10),
                Van: random.randint(2, 10),
                Convertible: random.randint(2, 10)
            }

            return self.__productionLot