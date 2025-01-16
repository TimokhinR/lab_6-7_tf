from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Math API!"

@app.route('/add/<float:a>/<float:b>')
def add(a, b):
    return str(a + b)

@app.route('/subtract/<float:a>/<float:b>')
def subtract(a, b):
    return str(a - b)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)

