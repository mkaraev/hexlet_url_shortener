import json

from flask import Flask, request

import storage
from entities import URL

app = Flask(__name__)


@app.route("/url/<string:url>", methods=["GET"])
def get_url(url: str):
    return json.dumps(storage.get_url(short_url=url).json())


@app.route("/url", methods=["POST"])
def post_url():
    payload = request.get_json()
    url = URL(**payload)
    url_json = storage.create_url(url).json()
    return json.dumps(url_json)


@app.route("/url/<string:url>", methods=["DELETE"])
def delete_url(url: str):
    return f"DELETED {url}"


if __name__ == '__main__':
    app.run(debug=True)
