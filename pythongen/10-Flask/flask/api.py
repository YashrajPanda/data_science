# Put and Delete-HTTP Verbs
# Working with API's-Json

from flask import Flask, jsonify, request
app=Flask(__name__)

# Initial Data in my to do list
item=[
    {"id": 1, "name":"Item 1", "description":"This is item 1"},
    {"id": 2,"name":"Item 2", "description":"This is item 2"},
]

@app.route("/")
def home():
    return "welcome to the simple To Do List App"

# Get: Retrieve all the items
@app.route("/")
def get