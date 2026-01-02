from flask.wrappers import Request
from ..errors.http_unprocessable_entity import HttpUnprocessableEntityError
from ..errors.http_bad_request import HttpBadRequestError

class Calculator1:
    def calculate(self, request: Request) -> dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3
        first_process = self.__first_process(splited_number)
        second_process = self.second_process(splited_number)
        calc_result = first_process + second_process + splited_number
        response = self.__format_response(calc_result)
        return response
    
    def __validate_body(self, body: dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("Missing 'number' in request body")
        input_data = body["number"]
        if not isinstance(input_data, (int, float)):
            raise HttpBadRequestError("'number' must be an integer or float")
        return float(input_data)
    
    def __first_process(self, number: float) -> float:
        return (((number / 4) + 7) ** 2) * 0.257
    
    def second_process(self, number: float) -> float:
        return ((number ** 2.121) / 5) + 1
    
    def __format_response(self, result: float) -> dict:
        return {"data": {
            "calculator": 1,
            "result": round(result, 2)
        }}