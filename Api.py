from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

films = {
    1: {"film": "Avatar", "duration": 2.7},
    2: {"film": "Alien", "duration": 1.8},
}
actors = {
    1: {'name': 'LeoDiCaprio', 'age': '48'},
    2: {'name': 'MarkRuffalo', 'age': '55'}
}

parser = reqparse.RequestParser()      # описываем в каком виде получаем инфо по фильмам
parser.add_argument("film", type=str)
parser.add_argument("duration", type=float)

class Main(Resource):    # клас по управлению сайтом
    def get(self, film_id):
        if film_id == 0:
            return films
        else:
            return films[film_id]

    def delete(self, film_id):
        del films[film_id]
        return films

    def post(self, film_id):
        films[film_id] = parser.parse_args()
        return films

    def put(self, film_id):
        films[film_id] = parser.parse_args()
        return films

    def get(self, actor_id):
        if actor_id == 0:
            return actors
        else:
            return actors[actor_id]

if api.add_resource(Main, "/api/films/<int:film_id>"):
    api.init_app(app)
elif api.add_resource(Main, "/api/actors/<int:actor_id>"):
    api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
