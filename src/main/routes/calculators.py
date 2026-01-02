from flask import Blueprint, jsonify, request
from ..factories.calculator1_factory import Calculator1Factory
from ..factories.calculator2_factory import Calculator2Factory
from ..factories.calculator3_factory import Calculator3Factory
from ...errors.error_controller import ErrorController

class CalculatorsRoutes():
    calc_route_bp = Blueprint('calc_routes', __name__)

    
    @calc_route_bp.route('/calculator/1', methods=['POST'])
    def __calculator_1():
        try:
            calc = Calculator1Factory.create()
            response = calc.calculate(request)
            return jsonify(response), 200
        except Exception as e:
            error = ErrorController.handle_errors(e)
            return jsonify(error["body"]), error["status_code"]
    
    @calc_route_bp.route('/calculator/2', methods=['POST'])
    def __calculator_2():
        try:
            calc = Calculator2Factory().create()
            response = calc.calculate(request)
            return jsonify(response), 200
        except Exception as e:
            error = ErrorController.handle_errors(e)
            return jsonify(error["body"]), error["status_code"]

    
    @calc_route_bp.route('/calculator/3', methods=['POST'])
    def __calculator_3():
        try:
            calc = Calculator3Factory().create()
            response = calc.calculate(request)
            return jsonify(response), 200
        except Exception as e:
            error = ErrorController.handle_errors(e)
            return jsonify(error["body"]), error["status_code"]