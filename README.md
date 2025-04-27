# Mini Project Management API 📊

This is a simple **Project Management API** built using **FastAPI**. The API provides the core functionality of managing projects, tasks, and users, while also implementing user authentication, role-based access control, and task management features.

---

## Features ✨

### Core Features:
- **User Authentication 🛂:**
  - Users can authenticate via **JWT-based tokens** to ensure secure login and access.
  
- **Projects 📂:**
  - **Create** new projects.
  - **Update** existing projects.
  - **Delete** projects.
  - **List** all projects.

- **Tasks 📝:**
  - **Assign tasks** to specific projects.
  - Set **deadlines ⏳**, **status** (To-Do, In Progress, Done), and **priority** (Low, Medium, High).
  - **Assign tasks** to users.

- **Filtering & Pagination 🔍:**
  - Tasks can be filtered by **project**, **status**, or **due date**.
  - Pagination is supported for listing tasks and projects.

### Bonus Features 🌟:
- **Role-based Access Control (RBAC):**
  - Users can have different roles: **admin 👑**, **project manager 🧑‍💻**, **developer 👨‍💻**.
  - The admin can manage all aspects of projects, while a project manager can only manage tasks for their assigned projects.

- **Database 🗃️:**
  - The application uses **PostgreSQL** for persistent data storage.
  
- **Dockerization 🐳:**
  - The application is containerized using **Docker**, allowing easy deployment and management in various environments.

- **Swagger/OpenAPI Documentation 📖:**
  - Automatic API documentation generated using **Swagger/OpenAPI** for easy testing and interaction with the API.

---

## Setup Instructions ⚙️

### Requirements:
- **Python 3.7+** 🐍
- **PostgreSQL** database 🗄️
- **Docker** 🐋 (for containerization)

### Installation 🛠️:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/project-management-api.git
   cd project-management-api
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL:**

   - Make sure you have **PostgreSQL** installed and running.
   - Create a new database (e.g., `project_management`).
   - Update the **DATABASE_URL** in the `.env` file.

5. **Run the application:**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API docs:**
   - Open `http://localhost:8000/docs` in your browser to interact with the API via the **Swagger UI**.

---

## Usage 📥:

### Authentication 🔐:

- **Register a user:**

  POST `/register/`

  Example Request Body:
  ```json
  {
    "username": "john_doe",
    "password": "password123"
  }
  ```

- **Login to get the access token:**

  POST `/login/`

  Example Request Body:
  ```json
  {
    "username": "john_doe",
    "password": "password123"
  }
  ```

  The response will include a **JWT** token that you can use for further requests.

---

### Projects 📋:

- **Create a project:**

  POST `/projects/`

  Example Request Body:
  ```json
  {
    "name": "Project A",
    "description": "This is a description of Project A"
  }
  ```

- **Get all projects:**

  GET `/projects/`

---

### Tasks 🗂️:

- **Create a task:**

  POST `/tasks/`

  Example Request Body:
  ```json
  {
    "name": "Task 1",
    "description": "This is the first task",
    "due_date": "2025-05-01T00:00:00",
    "status": "To-Do",
    "priority": "Medium",
    "project_id": 1,
    "assignee_id": 2
  }
  ```

- **Get all tasks with filters:**

  GET `/tasks/`

  Example Request Parameters:
  - `project_id=1`
  - `status=To-Do`

---

## Role-based Access Control 🛡️:

- **Admin 👑** users can manage all projects and tasks.
- **Project Managers 🧑‍💻** can manage only tasks within the projects they oversee.
- **Developers 👨‍💻** can only view and update tasks assigned to them.

---

## Dockerization 🐳

The project comes with a **Dockerfile** and **docker-compose.yml** file for easy containerization. To run the application inside a Docker container:

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Start the container:

   ```bash
   docker-compose up
   ```

The application will be accessible at `http://localhost:8000` in your browser.

---

## License 📜

This project is licensed under the **MIT License**.

---

## Conclusion 🎉

This project demonstrates the ability to design and implement a full-featured RESTful API using **FastAPI** with features like user authentication, task management, and role-based access control. It's easy to deploy using Docker and works with **PostgreSQL** for persistent data storage.
