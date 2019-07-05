""" app.py """
from flask import Flask, Blueprint, jsonify
from server.config import config

app = Flask(__name__)
core_blueprint = Blueprint('core', __name__)


@core_blueprint.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Project Klima'}), 200

app.register_blueprint(core_blueprint)

if __name__ == '__main__':
    is_debug = config.environment != 'production'
    app.run(host=config.app_host, debug=is_debug)
