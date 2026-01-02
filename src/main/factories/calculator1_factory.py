from ...calculators.calculator_1 import Calculator1

class Calculator1Factory():
    @staticmethod
    def create() -> Calculator1:
        return Calculator1()