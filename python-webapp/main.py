from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append({'text': todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:index>', methods=['GET', 'POST'])
def toggle(index):
    if 0 <= index < len(todos):
        todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
