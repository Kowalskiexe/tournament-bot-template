from flask import Flask, request, json
from bot import strategy


app = Flask(__name__)


@app.route('/', methods=['POST'])
def play():
    body = json.loads(request.data)
    opponents_move = body['opponents_last_move']
    return json.dumps({"my_move": strategy.play(opponents_move)})

