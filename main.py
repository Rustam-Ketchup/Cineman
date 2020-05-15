from imdb import IMDb
from flask import Flask, request, render_template
from kinopoisk.movie import Movie
import json
from parsers import IviParser, MegogoParser
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

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


@app.route('/api/get-search-results/', methods=['post'])
def api_imdb():
    name = request.data.film
    ia = IMDb()
    results = ia.search_movie(name)
    data = []
    ivi = IviParser()
    megogo = MegogoParser()
    data.append(ivi.IviFind(name))
    data.append(megogo.MegogoFind(name))
    for result in results:
        ia.update(result)
        movie = {}
        if 'title' in result.keys():movie['title'] = result['title']
        if 'rating' in result.keys(): movie['rating'] = result['rating']
        if 'votes' in result.keys(): movie['votes'] = result['votes']
        if 'full-size cover url' in result.keys(): movie['image'] = result['full-size cover url']
        data.append(movie)
    return json.dumps(data) # str(results)


if __name__ == "__main__":
    app.run(debug=True)
