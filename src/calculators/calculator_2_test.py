from .calculator_2 import Calculator2
from ..drivers.numpy_handler import NumpyHandler
from ..drivers.interfaces.driver_handler_interface import IDriverHandler

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body

class MockDriverHandler(IDriverHandler):
    def standard_derivation(self, numbers: list[float]):
        return 3
    def variance(self, numbers: list[float]):
        ...

# Integração entre NumpyHandler e Calculator2
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    calculator_2 = Calculator2(driver_handler=NumpyHandler())
    formatted_response = calculator_2.calculate(mock_request)
    assert isinstance(formatted_response, dict)
    assert formatted_response == {'data': {'calculator': 2, 'result': 0.08}}

def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    calculator_2 = Calculator2(driver_handler=MockDriverHandler())
    formatted_response = calculator_2.calculate(mock_request)
    assert isinstance(formatted_response, dict)
    assert formatted_response == {'data': {'calculator': 2, 'result': 0.33}}
