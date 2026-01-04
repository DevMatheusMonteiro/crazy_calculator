from flask.wrappers import Request
from ..errors.http_unprocessable_entity import HttpUnprocessableEntityError
from ..errors.http_bad_request import HttpBadRequestError

class Calculator4:
    def calculate(self, request: Request) -> dict:
        body = request.json
        input_data = self.__validate_body(body)
        result = self.__calculate_average(input_data)
        return self.__format_response(result)
    
    def __validate_body(self, body: dict) -> list[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Missing 'numbers' in request body")
        input_data = body.get("numbers")
        return input_data
    
    def __calculate_average(self, input_data: list[float]) -> float:
        return sum(input_data) / len(input_data)

    def __format_response(self, result: float) -> dict:
        return {"data": {
            "calculator": 4,
            "value": result,
            "success": True
        }}