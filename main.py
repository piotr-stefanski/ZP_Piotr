from flask import Flask
from flask_restful import Api
from services.api_resources import MoviesResource

app = Flask(__name__)
api = Api(app)

api.add_resource(MoviesResource, '/movies')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')












'''
TODO:
- zasoby z pliku movies.csv dostępne pod endpointem /movies
- dodanie nowych modeli danych dla reszty danych (links, ratings, tags)
- dodanie nowych endpointow (/links, /ratings, /tags)
'''