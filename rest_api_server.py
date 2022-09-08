import json
from flask import Flask
from app import get_words_histogram

app = Flask(__name__)


@app.route('/getHistogram', methods=['GET'])
def get_histogram():
    result = get_words_histogram()
    return json.dumps(result)


def run_flask():
    app.run()

