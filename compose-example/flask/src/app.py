from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for
import os
from pymongo import MongoClient

app = Flask(__name__)


db_host = os.environ.get("DB_HOST", "localhost")

client = MongoClient(host=f"mongodb://{db_host}:27017/")
db = client.get_database("tododb")

def load_todos():
    entries = []
    for todo in db.todos.find():
        todo["_id"] = str(todo["_id"])
        entries.append(todo)
    return entries

def save_todos(todo):
    db.todos.insert_one(todo)

@app.route("/")
def index():
    return render_template("index.html", todos=load_todos())

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("todo")
    if text:
        save_todos({
            "text": text,
            "done": False
        })
    return redirect(url_for("index"))

@app.route("/toggle/<string:todo_id>", methods=["POST"])
def toggle(todo_id):
    todo = db.todos.find_one({
            "_id": ObjectId(todo_id)
        })

    print("A")

    if todo:
        db.todos.update_one(
                {"_id": ObjectId(todo_id)},
                {"$set": {"done": not todo.get("done")}}
        )

    return redirect(url_for("index"))
