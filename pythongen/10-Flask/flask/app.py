from flask import Flask
'''
It creates an instance of the Flask class
Which will be our WSGI application.
'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask Application!, i am yash, i love python and flask"

@app.route("/index")
def index():
    return "This is the index page of the Flask Application."

@app.route("/about")
def about():
    return "This is the about page of the Flask Application."

if __name__ == "__main__":
    app.run(debug=True)
    # The debug=True flag enables the debug mode, which provides a debugger and reloader.
    # This is useful during development to automatically reload the server on code changes.
    