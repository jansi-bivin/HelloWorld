from flask import Flask

# create the flask application
app = Flask(__name__)

# home route
@app.route('/')
def home():
    return "Hello, Flask!"

# about route
@app.route('/about')
def about():
    return "This is a simple Flask app example."

if __name__ == '__main__':
    app.run(debug=True)
