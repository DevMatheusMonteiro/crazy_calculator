from .calculator_4 import Calculator4

from pytest import raises

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({"numbers": [1,2,3,4,5]})
    calculator_4 = Calculator4()
    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'calculator': 4, 'value': 3.0, 'success': True}}