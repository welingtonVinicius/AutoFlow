import React, { useState } from 'react';

export const AddTaskForm = ({ onTaskAdd }) => {
  const [taskTitle, setTaskTitle] = useState('');
  const [taskDescription, setTaskDescription] = useState('');
  const [taskWorkflow, setTaskWorkflow] = useState('');

  const handleFormSubmit = (event) => {
    event.preventDefault();
    
    if (!taskTitle || !taskDescription || !taskWorkflow) {
      alert('Please fill in all the fields.');
      return;
    }

    onTaskAdd({ title: taskTitle, description: taskDescription, workflow: taskWorkflow });
    setTaskTitle('');
    setTaskDescription('');
    setTaskWorkflow('');
  };

  return (
    <form onSubmit={handleFormSubmit}>
      <input
        type="text"
        placeholder="Title"
        value={taskTitle}
        onChange={(e) => setTaskTitle(e.target.value)}
      />
      <input
        type="text"
        placeholder="Description"
        value={taskDescription}
        onChange={(e) => setTaskDescription(e.target.value)}
      />
      <input
        type="text"
        placeholder="Workflow"
        value={taskWorkflow}
        onChange={(e) => setTaskWorkflow(e.target.value)}
      />
      <button type="submit">Add Task</button>
    </form>
  );
};

export const TaskListView = ({ tasks }) => {
  return (
    <div>
      {tasks.map((task, index) => (
        <div key={index}>
          <h4>{task.title}</h4>
          <p>Description: {task.description}</p>
          <p>Workflow: {task.workflow}</p>
        </div>
      ))}
    </div>
  );
};