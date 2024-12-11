import React, { useState, useEffect } from 'react';

export const TaskForm = ({ onAdd }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [workflow, setWorkflow] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title || !description || !workflow) {
      alert('Please provide all required fields');
      return;
    }
    onAdd({ title, description, workflow });
    setTitle('');
    setDescription('');
    setWorkflow('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} />
      <input type="text" placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
      <input type="text" placeholder="Workflow" value={workflow} onChange={(e) => setWorkflow(e.target.value)} />
      <button type="submit">Add Task</button>
    </form>
  );
};

export const TaskList = ({ tasks }) => {
  return (
    <div>
      {tasks.map((task, index) => (
        <div key={index}>
          <h3>{task.title}</h3>
          <p>{task.description}</p>
          <p>{task.workflow}</p>
        </div>
      ))}
    </div>
  );
};
