from imdb import IMDb
from flask import Flask, request, render_template, Response
from kinopoisk.movie import Movie
import json
from parsers import IviParser, MegogoParser
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['post', 'get'])
def index():
    ia = IMDb()
    results = ia.search_movie('the matrix')
    for result in results:
        print(result.movieID, result)
    matrix = results[0]
    ia.update(matrix)
    print(matrix.keys())
    return render_template('index.html', title='', description='', year='', critic='')


@app.route('/api/get-serch-results/', methods=['post', "get", 'options'])
@cross_origin()
def api_imdb():
    name = json.loads(request.data.decode('utf8').replace("'", '"'))
    name = name["film"]

    data = []

    ivi_data = IviParser.IviFind(name)
    megogo_data = MegogoParser.MegogoFind(name)

    for ivi_film in ivi_data:
        data.append(ivi_film)
    for megogo_film in megogo_data:
        data.append(megogo_film)
    print(data)

    return json.dumps(data)


if __name__ == "__main__":
    app.run(debug=True)
