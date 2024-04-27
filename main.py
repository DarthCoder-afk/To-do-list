from flask import Flask, request, jsonify

app = Flask(__name__)


tasks = {
    "1": {"title": "Task 1", "description": "Complete assignment"},
    "2": {"title": "Task 2", "description": "Buy groceries"}
}

@app.route("/get-task/<task_id>", methods=["GET"])
def get_task(task_id):
    if task_id in tasks:
        return jsonify(tasks[task_id]), 200
    else:
        return jsonify({"error": "Task not found"}), 404


@app.route("/create-task", methods=["POST"])
def create_task():
    data = request.get_json()
    if "title" in data and "description" in data:
        task_id = str(len(tasks) + 1)
        tasks[task_id] = {"title": data["title"], "description": data["description"]}
        return jsonify({"task_id": task_id}), 201
    else:
        return jsonify({"error": "Missing title or description in request body"}), 400


@app.route("/update-task/<task_id>", methods=["PUT"])
def update_task(task_id):
    if task_id in tasks:
        data = request.get_json()
        tasks[task_id]["title"] = data.get("title", tasks[task_id]["title"])
        tasks[task_id]["description"] = data.get("description", tasks[task_id]["description"])
        return jsonify(tasks[task_id]), 200
    else:
        return jsonify({"error": "Task not found"}), 404


@app.route("/delete-task/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return jsonify({"message": "Task deleted successfully"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
