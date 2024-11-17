import React, { useState, useEffect } from 'react';

export const WorkflowForm = ({ onSubmit }) => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!name || !description) {
      alert('Please fill in all fields');
      return;
    }
    onSubmit({ name, description });
    setName('');
    setDescription('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Name"
          required
        />
      </div>
      <div>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Description"
          required
        />
      </div>
      <button type="submit">Create Workflow</button>
    </form>
  );
};

export const WorkflowList = ({ workflows, onWorkflowSelect }) => {
  return (
    <ul>
      {workflows.map((workflow) => (
        <li key={workflow.id} onClick={() => onWorkflowSelect(workflow)}>
          {workflow.name}
        </li>
      ))}
    </ul>
  );
};

export const WorkflowDetail = ({ selectedWorkflow, onTaskUpdate }) => {
  const [newTask, setNewTask] = useState('');

  const addTask = () => {
    if (!newTask) {
      alert('Please enter a task name');
      return;
    }
    onTaskUpdate([...selectedWorkflow.tasks, { name: newTask, status: 'pending' }]);
    setNewTask('');
  };

  if (!selectedWorkflow) return <div>Select a workflow to see details</div>;

  return (
    <div>
      <h2>{selectedWorkflow.name}</h2>
      <h3>Tasks</h3>
      {selectedWorkflow.tasks.map((task, index) => (
        <div key={index}>{task.name} - {task.status}</div>
      ))}
      <div>
        <input
          type="text"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          placeholder="New task name"
        />
        <button onClick={addTask}>Add Task</button>
      </div>
    </div>
  );
};