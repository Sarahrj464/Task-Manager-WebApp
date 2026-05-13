// load Tasks
async function loadTasks(filter = "all") {
  const response = await fetch(`/api/tasks?filter=${filter}`);
  const data = await response.json();
  console.log(data);
  renderTasks(data.tasks);
  updateStats(data);
}

function renderTasks(tasks) {
  const list = document.getElementById("task-list");

  if (tasks.length === 0) {
    list.innerHTML = "<li>No Tasks Found!</li>";
    return;
  }

  list.innerHTML = tasks
    .map(
      (task) =>
        `<li>
            <span>${task.title}</span>
            <div class="task-actions">
              <button class="btn-toggle" onclick="toggleTask(${task.id})">${task.completed ? "↩ Undo" : "✅ Done"}</button>
              <button class="btn-delete" onclick="deleteTask(${task.id})"> 🗑 Delete</button>
            </div>
        </li>`,
    )
    .join("");
}

loadTasks();

// Update stats
function updateStats(data) {
  let stats = document.getElementById("stats");
  stats.innerHTML = `Total ${data.total} | Completed ${data.completed} | Remaining ${data.remaining}`;
}

// Delete task
async function deleteTask(id) {
  // confirm popup
  if (!confirm("Delete this task?")) return;

  const response = await fetch(`/api/tasks/${id}`, {
    method: "DELETE",
  });

  loadTasks();
}

// toggle task
async function toggleTask(id) {
  const response = await fetch(`/api/tasks/${id}/toggle`, {
    method: "PATCH",
  });

  loadTasks();
}

// add task
async function addTask() {
  const task = document.getElementById("task-input");
  if (task.value.trim() == "") {
    alert("Task not added");
    return;
  }

  const response = await fetch(`/api/tasks`, {
    method: "POST",
    headers: { "Content-type": "application/json" },
    body: JSON.stringify({ title: task.value.trim() }),
  });

  // input task empty
  task.value = "";

  loadTasks();
}
