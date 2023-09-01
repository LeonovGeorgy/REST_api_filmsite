from flask import Flask, request
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

parser = reqparse.RequestParser()# описываем в каком виде получаем инфо по фильмам
parser.add_argument("film", type=str)
parser.add_argument("duration_min", type=int)
parser.add_argument("country", type=str)
parser.add_argument("fees_mill$", type=float)

class Main(Resource):    # клас по управлению сайтом
    def get(self, site_id):         # получаем инфо по ссылке
        if site_id == 0:
            return films
        else:
            return films[site_id]

    def delete(self, site_id):      # удалить ссылку
        del films[site_id]
        return films

    #def post(self, site_id):        # добавить новую ссылку
        #films[site_id] = parser.parse_args()
        #return films
    def post(self, site_id):
        data = parser.parse_args()
        if site_id not in films:
            films[site_id] = {}
        if data["film"]:
            films[site_id]["film"] = data["film"]
            films[site_id]["duration_min"] = data["duration_min"]
        elif data["country"]:
            films[site_id]["country"] = data["country"]
            films[site_id]["fees_mill$"] = data["fees_mill$"]
        return films

    def put(self, site_id):         # обновить имеющуюся
        data = parser.parse_args()
        if site_id not in films:
            films[site_id] = {}
        if data["film"]:
            films[site_id]["film"] = data["film"]
            films[site_id]["duration_min"] = data["duration_min"]
        elif data["country"]:
            films[site_id]["country"] = data["country"]
            films[site_id]["fees_mill$"] = data["fees_mill$"]
        return films


api.add_resource(Main, "/api/films/<int:site_id>")
api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
