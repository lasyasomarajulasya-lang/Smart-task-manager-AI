from flask import Flask, request, jsonify, render_template
from database import get_all_tasks, add_task, delete_task, complete_task
from analytics import suggest_priority

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/tasks", methods=['GET'])
def get_tasks():
    all_tasks = get_all_tasks()
    return jsonify([task.to_dict() for task in all_tasks])

@app.route("/add_task", methods=['POST'])
def create_task():
    data = request.json
    
    if data['priority'] == 'Auto':
        data['priority'] = suggest_priority(data['title'], data['description'])
    
    task = add_task(data['title'], data['description'], data['priority'])
    return jsonify(task.to_dict())

@app.route("/delete_task/<int:task_id>", methods=['DELETE'])
def remove_task(task_id):
    delete_task(task_id)
    return jsonify({"message": "Task deleted successfully"})

@app.route("/complete_task/<int:task_id>", methods=['PUT'])
def mark_complete(task_id):
    complete_task(task_id)
    return jsonify({"message": "Task status updated"})

if __name__ == "__main__":
    app.run(debug=True)