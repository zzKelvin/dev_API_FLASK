from flask_restful import Resource

habilidades = ['Python','Java','Flash','PHP']

class Habilidades(Resource):
    def get(self):
        return habilidades
