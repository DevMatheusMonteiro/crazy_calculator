from .calculator_3 import Calculator3
from ..drivers.interfaces.driver_handler_interface import IDriverHandler
from pytest import raises

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body

class MockDriverHandlerError(IDriverHandler):
    def standard_derivation(self, numbers: list[float]):
        ...
    def variance(self, numbers: list[float]):
        return 1

class MockDriverHandlerSuccess(IDriverHandler):
    def standard_derivation(self, numbers: list[float]):
        ...
    def variance(self, numbers: list[float]):
        return 1000000

def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1,2,3,4,5]})
    calculator_3 = Calculator3(MockDriverHandlerError())
    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "Process failure: variance is less than the multiplication"

def test_calculate():
    mock_request = MockRequest({"numbers": [1,1,1,1,100]})
    calculator_3 = Calculator3(MockDriverHandlerSuccess())
    response = calculator_3.calculate(mock_request)

    assert response == {'data': {'calculator': 3, 'value': 1000000, 'success': True}}
    