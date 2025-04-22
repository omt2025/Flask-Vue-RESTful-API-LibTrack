# 📚 LibTrack: Book Information Management System

A full-stack, RESTful book management application built with **Flask**, **Vue 3**, and **Element Plus**. This project demonstrates a clean separation of front-end and back-end with API-driven interaction using **Axios**.

---

## 🚀 Features

- 📖 Add, edit, delete, and view book records
- 🔍 Search and filter functionality (front-end)
- 🛠️ RESTful API endpoints with Flask
- 💾 SQLite database integration
- 🎨 Responsive UI with Vue and Element Plus
- 🔗 Frontend-backend separation via Axios

---

## 🧰 Tech Stack

| Layer       | Technology              |
|-------------|--------------------------|
| Backend     | Flask, Flask-SQLAlchemy  |
| Frontend    | Vue 3, Element Plus      |
| API Client  | Axios                    |
| Database    | SQLite                   |
| Dev Tools   | PyCharm, VSCode, Git     |

---

## 📂 Project Structure

```bash
LibTrack/
├── app.py                # Flask app entry
├── models.py             # Database models
├── extension.py          # DB extensions and setup
├── instance/books.sqlite # SQLite database
├── view_db.py            # Utility script to inspect DB
├── frontend/             # Vue project
│   ├── src/
│   └── ...
└── README.md
