from flask import Flask, render_template, redirect, url_for, request, abort

app=Flask(__name__)

tasks = [
    {"id": 1, "title": "Read a chapter of a book", "completed": False},
    {"id": 2, "title": "Clean the kitchen", "completed": True},
    {"id": 3, "title": "Write a blog post", "completed": False},
    {"id": 4, "title": "Water the plants", "completed": True},
    {"id": 5, "title": "Reply to emails", "completed": False}
]

@app.route('/')
def home():
    return redirect(url_for('todo'))

@app.route('/todos')
def todo():
    return render_template("todos.html", tasks=tasks)

@app.route('/toggle/<int:id>')
def toggle_complete(id):
    for task in tasks:
        if task["id"] == id:
            task["completed"] = not task["completed"]
            break
    return redirect(url_for('todo'))


@app.route('/add', methods=['GET','POST'])
def add_task():
    if request.method == 'POST':
        title = request.form["title"]
        new_task = {
            "id": len(tasks) + 1,
            "title": title,
            "completed": False
        }
        tasks.append(new_task)
        return redirect(url_for('todo'))
    return render_template("add_task.html")

@app.route('/delete/<int:id>')
def delete_task(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            break
    return redirect(url_for('todo'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    for task in tasks:
        if task["id"] == id:
            if request.method == 'POST':
                task["title"] = request.form["title"]
                return redirect(url_for('todo'))
            return render_template("edit.html", task=task)
    abort(404)

if __name__=='__main__':
    app.run(debug=True)


