from ...calculators.calculator_3 import Calculator3
from ...drivers.numpy_handler import NumpyHandler

class Calculator3Factory():
    @staticmethod
    def create() -> Calculator3:
        return Calculator3(NumpyHandler())