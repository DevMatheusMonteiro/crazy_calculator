from flask.wrappers import Request
from ..drivers.interfaces.driver_handler_interface import IDriverHandler

class Calculator3:
    def __init__(self, driver_handler: IDriverHandler) -> None:
        self.__driver_handler = driver_handler
    def calculate(self, request: Request) -> dict:
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_result(variance, multiplication)
        return self.__format_response(variance)



    def __validate_body(self, body: dict) -> list[float]:
        if "numbers" not in body:
            raise ValueError("Missing 'numbers' in request body")
        input_data = body.get("numbers")
        return input_data
    
    def __calculate_variance(self, input_data: list[float]) -> float:
        return self.__driver_handler.variance(input_data).__float__()
    
    def __calculate_multiplication(self, numbers: list[float]) -> float:
        multiplication = 1
        for number in numbers: multiplication *= number
        return multiplication

    def __verify_result(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception("Process failure: variance is less than the multiplication")

    def __format_response(self, variance: float) -> dict:
        return {"data": {
            "calculator": 3,
            "value": variance,
            "success": True
        }}