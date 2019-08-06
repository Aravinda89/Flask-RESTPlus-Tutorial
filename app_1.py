# App 1

from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

languages = []
python = {'language' : 'Python'}
languages.append(python)


@api.route('/language')
class Language(Resource):
	def get(self):
		return languages


if __name__ == '__main__':
	app.run(debug=True)


