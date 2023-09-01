from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

# Как бы наш сайт.
# В файле локал пропишем команды, как если бы нажимали на ссылки.
films = {
    1: {"film": "Batman Begins", "duration_min": 140},
    2: {"country": "USA", "fees_mill$": 205},
    3: {'Christian Bale': 'Batman', 'Michael Caine': 'Alfred'}
}

parser = reqparse.RequestParser()      # описываем в каком виде получаем инфо по фильмам
parser.add_argument("film", type=str)
parser.add_argument("duration", type=float)

class Main(Resource):    # клас по управлению сайтом
    def get(self, film_id):         # получаем инфо по ссылке
        if film_id == 0:
            return films
        else:
            return films[film_id]

    def delete(self, film_id):      # удалить ссылку
        del films[film_id]
        return films

    def post(self, film_id):        # добавить новую ссылку
        films[film_id] = parser.parse_args()
        return films

    def put(self, film_id):         # обновить имеющуюся
        films[film_id] = parser.parse_args()
        return films


api.add_resource(Main, "/api/films/<int:film_id>")
api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
