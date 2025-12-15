from flask.wrappers import Request

class Calculator1:
    def calculate(self, request: Request) -> dict:
        body = request.json
        input_data = self.__validate_body(body)

        splited_number = input_data / 3
        first_process = self.__first_process(splited_number)
        

    def __validate_body(self, body: dict) -> float:
        if "number" not in body:
            raise ValueError("Missing 'number' in request body")
        input_data = body["number"]
        if not isinstance(input_data, (int, float)):
            raise TypeError("'number' must be an integer or float")
        return float(input_data)
    
    def __first_process(self, number: float) -> float:
        first_part = (number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part