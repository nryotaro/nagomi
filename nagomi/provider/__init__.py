import flask as f

app = f.Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, world'