from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome"

@app.route('/play/<int:x>')
def squares(x):
    return render_template("index.html", num_boxes=x)

if __name__ == "__main__":
    app.run(debug=True)
