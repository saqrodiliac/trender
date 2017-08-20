from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8100, debug=True)
