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
# or
```bash
source venv/bin/activate   # On macOS/Linux
```
```bash pip install -r requirements.txt
```

2. Configure Environment
Copy .env.example as .env and fill with your MongoDB URI and JWT secret:
```bash
MONGO_URI=mongodb+srv://youruser:yourpass@cluster0.mongodb.net/
JWT_SECRET=your_super_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

