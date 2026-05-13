# TaskFlow 📝

A minimal and elegant **Task Manager web application** built with Python Flask and SQLite. Stay organized — add, complete, undo, and delete your daily tasks in a clean dark-themed interface.

---

## 🖥️ Preview

![TaskFlow Screenshot](screenshots/taskflow.JPG)

---

## ✨ Features

- ➕ Add new tasks instantly
- ✅ Mark tasks as **Done**
- ↩️ Undo completed tasks back to pending
- 🗑️ Delete tasks
- 🔢 Live task counter — Total | Completed | Remaining
- 🔍 Filter tasks by **All / Completed / Pending**
- 💾 Persistent storage with SQLite database
- 🌙 Clean dark-themed UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| Database | SQLite |
| Frontend | HTML5, CSS3 |
| API calls | JavaScript Fetch API |

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Sarahrj464/Task-Manager-WebApp.git
cd Task-Manager-WebApp
```

**2. Install dependencies**
```bash
pip install flask
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
Task-Manager-WebApp/
│
├── static/
│   ├── app.js        # Fetch API calls
│   └── style.css     # Dark theme styling
│
├── templates/
│   ├── index.html    # Main task page
│   └── edit.html     # Edit task page
│
├── app.py            # Flask routes & API
├── database.py       # SQLite database logic
└── task.db           # Auto-generated database
```

---

## 👩‍💻 Author

**Sarah** — passionate about building real projects while learning web development.

[![GitHub](https://img.shields.io/badge/GitHub-Sarahrj464-181717?logo=github&logoColor=white)](https://github.com/Sarahrj464)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask&logoColor=white)
