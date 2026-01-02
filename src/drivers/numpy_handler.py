import numpy
from typing import List
from .interfaces.driver_handler_interface import IDriverHandler
# Facade
class NumpyHandler(IDriverHandler):
    def __init__(self) -> None:
        self.__np = numpy
    
    def standard_derivation(self, numbers: list[float]) -> float:
        return self.__np.std(numbers)
    
    def variance(self, numbers: list[float]) -> float:
        return self.__np.var(numbers)