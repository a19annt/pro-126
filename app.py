from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/Hello')
def hello_world():
    return 'Hello World'

tasks = [
    {
        'id':1,
        'title':'attend classes',
        'description':'Orphicy Bridge Course',
        'done':False
    },
    {
        'id':2,
        'title':'go Running',
        'description':'walking and sprinting for 1 hr',
        'done' : False
    }
    ] 
@app.route("/add-task", methods=["POST"])
def add_task():
    task = {
        "id": tasks[-1]["id"] + 1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False
    }
    tasks.append(task)

    return jsonify({
        "status" : "success",
        "message": "Task added successfully !"
    })
@app.route('/get-task')
def get_task():
    return jsonify({
        'data':tasks
    })
if(__name__ == '__main__'):
    app.run(debug = True)