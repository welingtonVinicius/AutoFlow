import React, { useState, useEffect } from 'react';

export const WorkflowCreationForm = ({ onWorkflowSubmit }) => {
  const [workflowName, setWorkflowName] = useState('');
  const [workflowDescription, setWorkflowDescription] = useState('');

  const handleFormSubmit = (event) => {
    event.preventDefault();
    if (!workflowName || !workflowDescription) {
      alert('Please fill in all fields');
      return;
    }
    onWorkflowSubmit({ name: workflowName, description: workflowDescription });
    setWorkflowName('');
    setWorkflowDescription('');
  };

  return (
    <form onSubmit={handleFormSubmit}>
      <div>
        <input
          type="text"
          value={workflowName}
          onChange={(e) => setWorkflowName(e.target.value)}
          placeholder="Name"
          required
        />
      </div>
      <div>
        <textarea
          value={workflowDescription}
          onChange={(e) => setWorkflowDescription(e.target.value)}
          placeholder="Description"
          required
        />
      </div>
      <button type="submit">Create Workflow</button>
    </form>
  );
};

export const WorkflowListView = ({ workflows, onSelectWorkflow }) => {
  return (
    <ul>
      {workflows.map((workflow) => (
        <li key={workflow.id} onClick={() => onSelectWorkflow(workflow)}>
          {workflow.name}
        </li>
      ))}
    </ul>
  );
};

export const WorkflowDetailsView = ({ selectedWorkflow, onUpdateTask }) => {
  const [taskName, setTaskName] = useState('');

  const handleAddTask = () => {
    if (!taskName) {
      alert('Please enter a task name');
      return;
    }
    onUpdateTask([...selectedWorkflow.tasks, { name: taskName, status: 'pending' }]);
    setTaskName('');
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
          value={taskName}
          onChange={(e) => setTaskName(e.target.value)}
          placeholder="New task name"
        />
        <button onClick={handleAddTask}>Add Task</button>
      </div>
    </div>
  );
};