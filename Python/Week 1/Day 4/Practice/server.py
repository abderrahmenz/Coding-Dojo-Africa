from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success():
    return "Dojo"

@app.route('/say/<string:banana>')
def hello(banana):
    return f"Hi {banana}"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    repeated_word = (word + '<br>') * num
    return f"Hello {repeated_word}"

if __name__ == "__main__":
    app.run(debug=True)
