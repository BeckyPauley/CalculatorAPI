from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Add(Resource):
    def post(self):
        numbers = request.get_json()
        answer = numbers['num1'] + numbers['num2']
        return {'Answer': answer}

class Subtract(Resource):
    def post(self):
        numbers = request.get_json()
        answer = numbers['num1'] - numbers['num2']
        return {'Answer': answer}

class Multiply(Resource):
    def post(self):
        numbers = request.get_json()
        answer = numbers['num1'] * numbers['num2']
        return {'Answer': answer}

class Divide(Resource):
    def post(self):
        numbers = request.get_json()
        answer = numbers['num1'] / numbers['num2']
        return {'Answer': answer}


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')


app.run(port=5000, debug=True)