import random

from model.cars.suv import SUV
from model.cars.coupe import Coupe
from model.cars.sedan import Sedan
from model.cars.hatchback import Hatchback
from model.cars.van import Van
from model.cars.convertible import Convertible
from model.vehicle import Vehicle
from typing import Final

class ProductionPlanner:

    def __init__(self):    
        self.__vehicleTypes : Final[list] = [
            SUV,
            Coupe,
            Sedan,
            Hatchback,
            Van,
            Convertible
        ]
        self.__lotSummary = {}

    def generateProductionLot(self):

        lot = []

        vehicleTypes = self.__vehicleTypes.copy()
        count = random.randint(3,len(vehicleTypes))

        pickedVehicleTypes = random.sample(self.__vehicleTypes, count)
        
        for vehicleType in pickedVehicleTypes:

            quantity = random.randint(2, 8)

            for _ in range(quantity):

                vehicle = vehicleType()
                configuration = random.randint(1, 4)
                match configuration:

                    case 1:
                        # Standard
                        pass

                    case 2:
                        vehicle.isPremium = True

                    case 3:
                        vehicle.isTuned = True

                    case 4:
                        vehicle.isPremium = True
                        vehicle.isTuned = True
                lot.append(vehicle)

        self.__lotSummary = {
            "SUV Cars": list(filter(lambda vehicle: isinstance(vehicle,SUV), lot)),
            "Coupe Cars": list(filter(lambda vehicle: isinstance(vehicle,Coupe), lot)),
            "Sedan Cars": list(filter(lambda vehicle: isinstance(vehicle,Sedan), lot)),
            "Hatchback Cars": list(filter(lambda vehicle: isinstance(vehicle,Hatchback), lot)),
            "Van Cars": list(filter(lambda vehicle: isinstance(vehicle,Van), lot)),
            "Convertible Cars": list(filter(lambda vehicle: isinstance(vehicle,Convertible), lot))
        }

        return lot

    def getlotSummary(self):
        return self.__lotSummary.copy()

    def printLot(self,lot: list[Vehicle]):

        if(self.__lotSummary == None):
            print("Create lot first")
            return

        print("The lot is composed by:")
        headers = ["Car type","Amount"]
        body = []
        for k, v in self.__lotSummary.items():
            body.append([k,len(v)])
        
        print(f"{headers[0]:<15}{headers[1]:>10}")
        print("-" * 25)

        for k, v in self.__lotSummary.items():
            print(f"{k:<15}{len(v):>10}")
