from imdb import IMDb
from flask import Flask, request, render_template
from kinopoisk.movie import Movie

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)


