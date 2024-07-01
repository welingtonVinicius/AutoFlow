from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.before_request
def handle_json():
    if request.is_json:
        request.get_json()

class Workflow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='workflow', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    workflow_id = db.Column(db.Integer, db.ForeignKey('workflow.id'),
        nullable=False)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Workflow Management System!"})

@app.route('/workflows', methods=['GET', 'POST'])
def manage_workflows():
    if request.method == 'POST':
        data = request.get_json()
        new_workflow = Workflow(name=data['name'])
        db.session.add(new_workflow)
        db.session.commit()
        return jsonify({"message": "Workflow created", "workflow": data}), 201
    elif request.method == 'GET':
        workflows = Workflow.query.all()
        workflows_data = [{"id": workflow.id, "name": workflow.name} for workflow in workflows]
        return jsonify(workflows_data)

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        data = request.get_json()
        new_task = Task(name=data['name'], workflow_id=data['workflow_id'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task created", "task": data}), 201
    elif request.method == 'GET':
        tasks = Task.query.all()
        tasks_data = [{"id": task.id, "name": task.name, "workflow_id": task.workflow_id} for task in tasks]
        return jsonify(tasksData)

if __name__ == '__main__':
    db.create_all()
    app.run(port=5000, debug=True)