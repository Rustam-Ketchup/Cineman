from flask import Flask, request
import json
from parsers import IviParser, MegogoParser
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

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
