from .calculator_2 import Calculator2
from ..drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    calculator_2 = Calculator2(driver_handler=NumpyHandler())
    formatted_response = calculator_2.calculate(mock_request)
    assert isinstance(formatted_response, dict)
    assert formatted_response == {'data': {'calculator': 2, 'result': 0.08}}
