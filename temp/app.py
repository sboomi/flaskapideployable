"""
Créer une API qui renvoit une liste de prénom
"""
from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

# GLOBAL VARIABLES

# ROUTES
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/name/')
def name():
    list_name = {
        'Name':['Clement',
                'Laura',
                'Maxime']
    }
    return jsonify(list_name)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# Core app: run `python app.py` in the terminal
if __name__ == "__main__":
    app.run(debug=True)