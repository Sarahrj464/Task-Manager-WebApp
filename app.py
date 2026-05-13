from flask import Flask, render_template, request, redirect, jsonify
import database

app = Flask(__name__)

# create db when app starts
database.create_table()

# ----> HOME ROUTE (show task)


@app.route('/')
def index():
    filter_type = request.args.get('filter', 'all')

    if filter_type == 'completed':
        tasks = database.get_completed_task()
    elif filter_type == 'pending':
        tasks = database.get_pending_task()
    else:
        tasks = database.get_data()

    total, completed, remaining = database.count_task()

    return render_template("index.html", tasks=tasks, total=total, completed=completed, remaining=remaining)


# ----> ADD TASK
@app.route('/add', methods=["POST"])
def add():
    title = request.form.get('title')
    database.add_task(title)
    return redirect('/')


# ----> DELETE TASK
@app.route('/delete/<int:id>')
def delete(id):
    database.delete_task(id)
    return redirect('/')


# ----> MARK TASK
@app.route('/toggle/<int:id>')
def toggle(id):
    database.toggle_task(id)
    return redirect('/')


# ----> EDIT TASK
@app.route('/edit/<int:id>')
def edit(id):
    tasks = database.get_data()
    task = None
    for t in tasks:
        if t[0] == id:
            task = t
            break

    return render_template("edit.html", task=task)


# ----> UPDATE TASK
@app.route('/update/<int:id>', methods=["POST"])
def update(id):
    new_task = request.form['title']
    database.update_task(id, new_task)
    return redirect('/')


# JSON API Routes
@app.route('/api/tasks', methods=["GET"])
def api_get_tasks():
    # 1. check either JS send filter
    filter_type = request.args.get('filter', 'all')
    if filter_type == 'completed':
        tasks = database.get_completed_task()
    elif filter_type == 'pending':
        tasks = database.get_pending_task()
    else:
        tasks = database.get_data()

    # 2. JS does not read tuple so convert data into dict
    task_list = [
        {
            'id': t[0],
            'title': t[1],
            'completed': bool(t[2])
        }
        for t in tasks
    ]

    # 3. count current stats
    total, completed, remaining = database.count_task()

    # 4. return in json
    return jsonify({
        "tasks": task_list,
        "total": total,
        "completed": completed,
        "remaining": remaining
    })


# delete tasks
@app.route('/api/tasks/<int:id>', methods=["DELETE"])
def api_delete_task(id):
    database.delete_task(id)
    return jsonify({"message": "Task Deleted"})


# toggle task
@app.route('/api/tasks/<int:id>/toggle', methods=["PATCH"])
def api_toggle_task(id):
    database.toggle_task(id)
    return jsonify({"message":"Task toggle"})


# add task
@app.route('/api/tasks', methods=["POST"])
def api_add_task():
    data=request.get_json()
    title=data.get('title','').strip()
    database.add_task(title)
    return jsonify({"message":"Task added"}),201



if __name__ == "__main__":
    app.run(debug=True)





  