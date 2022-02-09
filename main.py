from flask import Flask
from flask_restful import Api

from framework.controller.ActionsController import ActionsController

app = Flask(__name__)
api = Api(app)

api.add_resource(ActionsController, '/actions')  # add endpoints

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)


