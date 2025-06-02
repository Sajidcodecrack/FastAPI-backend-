# FastAPI-backend-
A basic user task management with login,jwt authentication and CRUD operation then deployed in render 
# FastAPI User-Task Manager API

A secure, production-ready backend API for user and task management, built with FastAPI, MongoDB Atlas, and JWT authentication.

---

##  Features

- **User Registration & Login** with password hashing
- **JWT authentication** for protected routes
- **Task Management:** Create, Read, Update, Delete (CRUD) for each authenticated user
- **Background Task Integration:** On task creation, triggers a simulated email (console log)
- **MongoDB Atlas** (async with Motor)
- **Pydantic validation** and clean error handling
- **Fully modular FastAPI architecture**
- **Public deployment on Render.com**

---

##  Live API & Documentation

- **Live Demo:** [https://fastapi-backend-1-wa76.onrender.com/docs](https://fastapi-backend-1-wa76.onrender.com/docs)
  # Live render: https://fastapi-backend-1-wa76.onrender.com
  # Postman Testing 
  # https://fastapi-backend-1-wa76.onrender.com/auth/register (Registration)
  # https://fastapi-backend-1-wa76.onrender.com/auth/Login    (Login)
  # https://fastapi-backend-1-wa76.onrender.com/tasks/        (Creat Task) (Post)
  # https://fastapi-backend-1-wa76.onrender.com/tasks/        (Get all your task) (GET)
  # https://fastapi-backend-1-wa76.onrender.com/tasks/{task_id} (Update the task) (PUT)
  # https://fastapi-backend-1-wa76.onrender.com/tasks/{task_id}  (Delete the task) (Delete)


---

## 🛠 Setup Instructions

### 1. Clone & Install

```bash
git clone https://github.com/Sajidcodecrack/FastAPI-backend-.git
cd FastAPI-backend-/user_task_manager
```
 ```bash 
python -m venv venv
venv\Scripts\activate
# On Windows
```
#or
```bash
source venv/bin/activate   # On macOS/Linux
```
```bash
pip install -r requirements.txt
```

2. Configure Environment
Copy .env.example as .env and fill with your MongoDB URI and JWT secret:
```bash
MONGO_URI=mongodb+srv://youruser:yourpass@cluster0.mongodb.net/
JWT_SECRET=your_super_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
# 3. Run Locally
```bash
uvicorn app.main:app --reload
```
# Visit http://localhost:8000/docs for Swagger UI.
# API Usage Example
# POST /auth/register
```bash
{
  "username": "exampleuser",
  "email": "example@email.com",
  "password": "yourpassword"
}
```
# 2. Login
# POST /auth/login
``` bash
{
  "email": "example@email.com",
  "password": "yourpassword"
}
```
Copy the access_token from the response.

# 3. Use the Token
# In Swagger, click Authorize and paste Bearer <token>

# In Postman, set header: Authorization: Bearer <token>
# 4. Create a Task
# POST /tasks/
``` bash
{
  "title": "My Task",
  "description": "Details...",
  "status": "pending",
  "due_date": "2025-06-20T10:00:00"
}
```
# Get a Single Task
# GET /tasks/{task_id}
```bash
{
  "id": "string",
  "title": "Finish Assignment",
  "description": "Complete FastAPI backend by Sunday",
  "status": "pending",
  "due_date": "2025-06-21T23:59:00",
  "created_at": "2025-06-10T15:34:00"
}
```
# Update a Task
# PUT /tasks/{task_id}
``` bash
{
  "title": "Finish Assignment (Updated)",
  "status": "completed"
}
```
# 5. Delete a Task
# DELETE /tasks/{task_id}
``` bash
{
  "detail": "Task deleted"
}
```
# Author
# Sajidcodecrack

This repo demonstrates modern backend architecture and production deployment with FastAPI. For questions or collaboration, open an issue or contact me.

# sajidahamedkhulna2000@gmail.com
