from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class WorkflowModel(db.Model):
    __tablename__ = 'workflows'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    current_status = Column(String(50), nullable=False)

    associated_tasks = relationship('TaskModel', backref='associated_workflow')

class TaskModel(db.Model):
    __tablename__='tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    workflow_id = Column(Integer, ForeignKey('workflows.id'), nullable=False)
    current  = Column(String(50), nullable=False)