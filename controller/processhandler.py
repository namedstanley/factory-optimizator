from model.vehicle import Vehicle
from model.cars.convertible import *
from model.cars.coupe import *
from model.cars.hatchback import *
from model.cars.sedan import *
from model.cars.suv import *
from model.cars.van import *
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

    def createVehicle(self, vehicle: Vehicle):

        standardComponents, premiumComponents, tuningComponents = self.__designer.designVehicleComponents(vehicle)

        vehicle = self.__assembler.assembleVehicle(
            vehicle,
            standardComponents,
            premiumComponents if vehicle.isPremium else {},
            tuningComponents if vehicle.isTuned else {}
        )

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

        def designVehicleComponents(self, vehicle: Vehicle) -> dict:
            self.__initStandardComponents()
            self.__initPremiumComponents()
            self.__initTuningComponents()

            standardComponents = {}
            for k, v in self.__standardComponents.items():
                standardComponents[k] = v
                standardComponents[k].price = float(v.price * vehicle.priceMultipliers.get(k, 1.0))
            premiumComponents = {}
            for k, v in self.__premiumComponents.items():
                premiumComponents[k] = v
                premiumComponents[k].price = float(v.price * vehicle.priceMultipliers.get(k, 1.0))
            tuningComponents = {}
            for k, v in self.__tuningComponents.items():
                tuningComponents[k] = v
                tuningComponents[k].price = float(v.price * vehicle.priceMultipliers.get(k, 1.0))
            
            return ( standardComponents, premiumComponents, tuningComponents )

    class Assembler:

        def __init__(self):
            pass

        def assembleVehicle(self, vehicle: Vehicle, standardComponents: dict, premiumComponents: dict, tuningComponents: dict) -> Vehicle:
            
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
                standardComponentsPrice += component.price
                standardComponentsTime += component.assembly_time

            for component in vehicle.premiumComponents.values():
                premiumComponentsPrice += component.price
                premiumComponentsTime += component.assembly_time

            for component in vehicle.tuningComponents.values():
                tuningComponentsPrice += component.price
                tuningComponentsTime += component.assembly_time
            
            vehicle.productionPrice = round(standardComponentsPrice + premiumComponentsPrice + tuningComponentsPrice, 2)
            vehicle.productionTime = round(standardComponentsTime + premiumComponentsTime + tuningComponentsTime, 2)

            return vehicle
