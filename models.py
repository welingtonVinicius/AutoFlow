from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class WorkflowModel(db.Model):
    __tablename__ = 'workflows'
    workflow_id = Column(Integer, primary_key=True)
    workflow_name = Column(String(255), nullable=False)
    workflow_description = Column(String(255), nullable=True)
    workflow_status = Column(String(50), nullable=False)

    associated_tasks = relationship('TaskModel', backref='associated_workflow', lazy='dynamic')

class TaskModel(db.Model):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    task_title = Column(String(255), nullable=False)
    task_description = Column(String(255), nullable=True)
    associated_workflow_id = Column(Integer, ForeignKey('workflows.workflow_id'), nullable=False)
    task_status = Column(String(50), nullable=False)