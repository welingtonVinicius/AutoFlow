const API_ENDPOINT = process.env.API_ENDPOINT || 'https://your-backend-api.com';

const fetchTasks = async () => {
  try {
    const response = await fetch(`${API_ENDPOINT}/tasks`);
    const data = await response.json();
    displayTasks(data);
  } catch (error) {
    console.error("Failed to fetch tasks:", error);
  }
};

const displayTasks = (tasks) => {
  const tasksContainer = document.getElementById('tasksContainer');
  tasksContainer.innerHTML = '';
  tasks.forEach(task => {
    const taskElement = document.createElement('div');
    taskElement.textContent = task.name;
    tasksContainer.appendChild(taskElement);
  });
};

const createTask = async (task) => {
  try {
    const response = await fetch(`${API_ENDPOINT}/tasks`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(task),
    });
    const newTask = await response.json();
    fetchTasks();
  } catch (error) {
    console.error("Failed to create task:", error);
  }
};

const updateTask = async (id, updates) => {
  try {
    const response = await fetch(`${API_ENDPOINT}/tasks/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(updates),
    });
    const updatedTask = await response.json();
    fetchTasks();
  } catch (error) {
    console.error("Failed to update task:", error);
  }
};

document.addEventListener('DOMContentLoaded', fetchTasks);

document.getElementById('createTaskForm').addEventListener('submit', (e) => {
  e.preventDefault();
  const taskNameInput = document.getElementById('taskName');
  createTask({ name: taskNameInput.value });
  taskNameInput.value = '';
});

document.getElementById('tasksContainer').addEventListener('click', (e) => {
  if (e.target.matches('.updateTaskButton')) {
    const taskId = e.target.getAttribute('data-task-id');
    const newTaskName = prompt("New task name:");
    if (newTaskName) {
      updateTask(taskId, { name: newTaskName });
    }
  }
});