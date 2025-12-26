from flask.wrappers import Request
from ..drivers.interfaces.driver_handler_interface import IDriverHandler

class Calculator2:
    def __init__(self, driver_handler: IDriverHandler) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: Request) -> dict:
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        formatted_response = self.__format_response(calculated_number)
        return formatted_response

    def __validate_body(self, body: dict) -> list[float]:
        if "numbers" not in body:
            raise ValueError("Missing 'number' in request body")
        input_data = body.get("numbers")
        return input_data
    def __process_data(self, input_data: list[float]):
        numbers = [(number * 11) ** 0.95 for number in input_data]
        result = self.__driver_handler.standard_derivation(numbers).__float__()
        return 1 / result
    
    def __format_response(self, result: float) -> dict:
        return {"data": {
            "calculator": 2,
            "result": round(result, 2)
        }}