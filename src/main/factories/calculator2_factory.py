from ...calculators.calculator_2 import Calculator2
from ...drivers.numpy_handler import NumpyHandler

class Calculator2Factory():
    @staticmethod
    def create() -> Calculator2:
        return Calculator2(NumpyHandler())