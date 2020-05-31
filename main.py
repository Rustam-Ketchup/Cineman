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
    print(request.data)
    name = json.loads(request.data.decode('utf8').replace("'", '"'))
    print(name)
    name = name["film"]

    # name = "matrix"
    ia = IMDb()
    results = ia.search_movie(name)
    data = []
    # ivi = IviParser()
    # megogo = MegogoParser()
    # data.append(ivi.IviFind(name))
    # data.append(megogo.MegogoFind(name))
    print("processing") #
    i = 0 #
    for result in results:
        print(str(i/len(results)*100) + "%") #
        i += 1 #
        ia.update(result)
        movie = {}
        if 'title' in result.keys():movie['title'] = result['title']
        if 'rating' in result.keys(): movie['rating'] = result['rating']
        if 'votes' in result.keys(): movie['votes'] = result['votes']
        if 'full-size cover url' in result.keys(): movie['image'] = result['full-size cover url']
        data.append(movie)

    print(data)

    return str(data)

if __name__ == "__main__":
    app.run(debug=True)
