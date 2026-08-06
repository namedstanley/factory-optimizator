from model.cars.suv import SUV
from model.cars.coupe import Coupe
from model.cars.sedan import Sedan
from model.cars.hatchback import Hatchback
from model.cars.van import Van
from model.cars.convertible import Convertible

from typing import Final

def getVechicleTypes() -> list:
    vechicleTypes : Final[list] = [ SUV, Coupe, Sedan, Hatchback, Van, Convertible ]
    return vechicleTypes