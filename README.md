# 📚 LibTrack: Book Information Management System

LibTrack is a full-stack, RESTful book management application built using **Flask** for the back-end, **Vue 3** for the front-end, and **Element Plus** for UI components. The application demonstrates a clean separation between the front-end and back-end, using an API-driven interaction model with **Axios** for HTTP requests.

This project allows users to manage book records with features like adding, editing, deleting, and viewing books, along with a powerful search and filter functionality.

---

## 🚀 Features

- 📖 **Add**, **edit**, **delete**, and **view** book records.
- 🔍 **Search and filter** functionality to find books by attributes (e.g., title, author, publisher).
- 🛠️ **RESTful API** for handling requests and interactions between the front-end and back-end.
- 💾 **SQLite database** integration for lightweight and easy-to-use storage.
- 🎨 **Responsive user interface** built with Vue 3 and Element Plus for a seamless experience on any device.
- 🔗 **Frontend-backend separation** via Axios to keep the architecture clean and maintainable.

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
├── app.py                # Flask app entry point; includes route handlers and API setup
├── models.py             # Database models (e.g., Book model) and schema definitions
├── extension.py          # Database extensions and setup, including initialization for Flask-SQLAlchemy
├── instance/books.sqlite # SQLite database file storing all book records
├── view_db.py            # Utility script to inspect or visualize the database contents
├── frontend/             # Vue.js project folder containing the front-end code
│   ├── src/              # Vue components, store, and router setup
│   └── ...
└── README.md             # Project documentation
