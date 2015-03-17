from flask import jsonify
from sn_core.commons.application import NodeServer

app = NodeServer(__name__)


@app.route('/')
def index():
    return 'Flask is running!'


@app.route('/data')
def names():
    data = {
        "first_names": ["John", "Jacob", "Julie", "Jenny"]
    }
    return jsonify(data)