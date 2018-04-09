from flask import Flask, request, jsonify, abort
import random
app = Flask(__name__)

strs = []

@app.route('/str', methhod=['POST'])

def post_tasks():
    if not request.json or not 'title' in request.json:
        abort(400)
    str = {
        'name' = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(randrange(10))
        }

    strs.append(str)
    return jsonify({'str': str}), 201
