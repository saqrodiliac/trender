from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Hayden!'

app.run(host='0.0.0.0', port=8100, debug=True)
