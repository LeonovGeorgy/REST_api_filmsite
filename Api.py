from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

films = {
    1: {"name": "Python", "video": 15},
    2: {"name": "Java", "video": 10}
}

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("video", type=int)

class Main(Resource):
    def get(self, films_id):
        if films_id == 0:
            return films
        else:
            return films[films_id]

    def delete(self, films_id):
        del films[films_id]
        return films

    def post(self, films_id):
        films[films_id] = parser.parse_args()
        return films

    def put(self, films_id):
        films[films_id] = parser.parse_args()
        return films

api.add_resource(Main, "/api/films/<int:films_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)