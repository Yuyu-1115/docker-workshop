from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

DATA_DIR = "/app/data"
DATA_LOC = os.path.join(DATA_DIR, "data.txt")

def load_todos():
    entries = []
    if os.path.exists(DATA_LOC):
        with open(DATA_LOC, "r") as f:
            for line in f.readlines():
                data = line.strip().split(":", 1)
                entry = {
                        "text": data[1],
                        "done": data[0] == "1"
                        }
                entries.append(entry)
    return entries

def save_todos(todos):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_LOC, "w") as f:
        for todo in todos:
            f.write(f"{1 if todo["done"] else 0}:{todo["text"]}\n")

@app.route("/")
def index():
    return render_template("index.html", todos=load_todos())

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("todo")
    todos = load_todos()
    if text:
        todos.append({
            "text": text,
            "done": False
            })
        save_todos(todos)
    return redirect(url_for("index"))

@app.route("/toggle/<int:index>", methods=["POST"])
def toggle(index):
    todos = load_todos()

    if 0 <= index < len(todos):
        todos[index]["done"] = not todos[index]["done"]
        save_todos(todos)
        
    return redirect(url_for("index"))
