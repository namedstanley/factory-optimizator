import random

from model.cars.suv import SUV
from model.cars.coupe import Coupe
from model.cars.sedan import Sedan
from model.cars.hatchback import Hatchback
from model.cars.van import Van
from model.cars.convertible import Convertible
from model.vehicle import Vehicle
from data.vehicletypes import getVechicleTypes

class ProductionPlanner:

    def __init__(self):
        self.__lot = []
        self.__lotSummary = {}
        self.__minNumOfVehicles = 3

    def generateProductionLot(self):

        vehicleTypes = getVechicleTypes()
        count = random.randint(
            self.__minNumOfVehicles
                if (len(vehicleTypes) >= self.__minNumOfVehicles)
                else len(vehicleTypes),
            len(vehicleTypes)
        )
        
        pickedVehicleTypes = random.sample(vehicleTypes, count)
        
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
                self.__lot.append(vehicle)

        self.__lotSummary = {
            "SUV Cars": list(filter(lambda vehicle: isinstance(vehicle,SUV), self.__lot)),
            "Coupe Cars": list(filter(lambda vehicle: isinstance(vehicle,Coupe), self.__lot)),
            "Sedan Cars": list(filter(lambda vehicle: isinstance(vehicle,Sedan), self.__lot)),
            "Hatchback Cars": list(filter(lambda vehicle: isinstance(vehicle,Hatchback), self.__lot)),
            "Van Cars": list(filter(lambda vehicle: isinstance(vehicle,Van), self.__lot)),
            "Convertible Cars": list(filter(lambda vehicle: isinstance(vehicle,Convertible), self.__lot))
        }

        return self.__lot.copy(), self.__lotSummary.copy()

    def getlotSummary(self):
        return self.__lotSummary.copy()

    def getlot(self):
        return self.__lot.copy()

    def setMinNumOfVehicles(self, num: int):
        self.__minNumOfVehicles = num

    def printLot(self):

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
