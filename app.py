from flask import Flask, render_template, jsonify
from flask_cors import CORS
import random

app = Flask(__name__,
            static_folder='./static/static')
CORS(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/getRandomNum')
def get_random_num():
    res = {
        'getRandomNum': random.randint(1, 100)
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run()
