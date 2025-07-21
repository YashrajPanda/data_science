from flask import Flask, render_template, request  
# render_template work is to render the HTML files

'''
It creates an instance of the Flask class
Which will be our WSGI application.
'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><body>Welcome to the Flask Application!<br>I am Yash, I love Python and Flask.</body></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}'
    return render_template("form.html")


@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}'
    return render_template("form.html")




if __name__ == "__main__":
    app.run(debug=True)
    # The debug=True flag enables the debug mode, which provides a debugger and reloader.
    # This is useful during development to automatically reload the server on code changes.
    