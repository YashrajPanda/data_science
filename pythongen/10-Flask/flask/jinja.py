# Building URL Dynamically
# Variable Rule
# Jinja 2 Template Engine

# Jinja2 Template Engine 
'''
Multiple ways for specifically for read the data source from the 
backend soruce

{{ }} print output in html
{%...%} conditions, for loop
{#...#} comments

'''

from flask import Flask, render_template, request, redirect, url_for
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


# @app.route("/submit",methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name}'
#     return render_template("form.html")

# # Variale Rule
# @app.route("/success/<int:score>")
# def success(score):
#     return "The marks you got is " + str(score)

# Variale Rule
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template("result.html",results=res)


@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
        
    exp={"score":score,"res":res}
    return render_template("result1.html",results=exp)

# If condition
@app.route("/successif/<int:score>")
def successif(score):
    
    return render_template("result.html",results=score)

@app.route("/fail/<int:score>")
def fail(score):
    
    return render_template("result.html",results=score)

@app.route("/getresults")
def get_result(score):
    return render_template("result.html", result=score)

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form["science"])
        math=float(request.form["maths"])
        c=float(request.form["c"])
        data_science=float(request.form["datascience"])
        total_score = (science + math + c + data_science) / 4
    else:
        return render_template("getresult.html")
        
    return redirect(url_for("successres", score=total_score))

if __name__ == "__main__":
    app.run(debug=True)
    # The debug=True flag enables the debug mode, which provides a debugger and reloader.
    # This is useful during development to automatically reload the server on code changes.
    