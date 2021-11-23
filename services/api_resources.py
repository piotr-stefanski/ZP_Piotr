from flask_restful import Resource
from services.repository import get_movies


class MoviesResource(Resource):
    def get(self):
        return get_movies()