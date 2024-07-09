from flask import Flask, Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///workflow.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Workflow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    tasks = db.relationship('Task', backref='workflow', lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    workflow_id = db.Column(db.Integer, db.ForeignKey('workflow.id'), nullable=False)


bp = Blueprint('workflow_app', __name__)

# Utility for error response
def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_config
    return response

@bp.route('/workflows', methods=['POST'])
def create_workflow():
    data = request.get_json()
    if not data or 'name' not in data:
        return error_response("Missing 'name' field.", 400)
    new_workflow = Workflow(name=data['name'])
    try:
        db.session.add(new_workflow)
        db.session.commit()
        return jsonify({'message': 'Workflow created', 'id': new_workflow.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return error_response(str(e.orig), 500)


@bp.route('/workflows/<int:id>', methods=['PUT'])
def update_workflow(id):
    data = request.get_json()
    if not data or 'name' not in data:
        return error_response("Missing 'name' field.", 400)
    workflow = Workflow.query.get_or_404(id)
    workflow.name = data['name']
    try:
        db.session.commit()
        return jsonify({'message': 'Workflow updated'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return error_response(str(e.orig), 500)


@bp.route('/workflows/<int:id>', methods=['DELETE'])
def delete_workflow(id):
    workflow = Workflow.query.get_or_404(id)
    try:
        db.session.delete(workflow)
        db.session.commit()
        return jsonify({'message': 'Workflow deleted'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return error_response(str(e.orig), 500)


@bp.route('/workflows', methods=['GET'])
def get_workflows():
    try:
        workflows = Workflow.query.all()
        return jsonify([{'id': w.id, 'name': w.name} for w in workflows]), 200
    except SQLAlchemyError as e:
        return error_response(str(e.orig), 500)


@bp.route('/workflows/<int:workflow_id>/tasks', methods=['POST'])
def create_task(workflow_id):
    data = request.get_json()
    if not data or 'name' not in data:
        return error_response("Missing 'name' field.", 400)
    new_task = Task(name=data['name'], workflow_id=workflow_id)
    try:
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created', 'id': new_task.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return error_response(str(e.orig), 500)


@bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    if not data or 'name' not in data:
        return error_response("Missing 'name' field.", 400)
    task = Task.query.get_or_404(id)
    task.name = data['name']
    try:
        db.session.commit()
        return jsonify({'message': 'Task updated'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return error_response(str(e.orig), 500)


@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return error_response(str(e.orig), 500)


@bp.route('/workflows/<int:workflow_id>/tasks', methods=['GET'])
def get_tasks(workflow_id):
    try:
        tasks = Task.query.filter_by(workflow_id=workflow_id).all()
        return jsonify([{'id': t.id, 'name': t.name} for t in tasks]), 200
    except SQLAlchemyError as e:
        return error_response(str(e.orig), 500)

app.register_blueprint(bp, url_prefix='/api')