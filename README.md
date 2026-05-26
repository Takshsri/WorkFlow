# Workflow Management System

A production-style backend Workflow Management System built using FastAPI, PostgreSQL, SQLAlchemy, and JWT Authentication with Role-Based Access Control (RBAC).

## Features

- User Signup & Login
- JWT Authentication
- Password Hashing using bcrypt
- Role-Based Access Control (Admin, Manager, Employee)
- Protected Routes
- User Profile Management
- Profile Update & Delete APIs
- PostgreSQL Integration
- SQLAlchemy ORM
- RESTful API Architecture

---

# Tech Stack

## Backend
- FastAPI

## Database
- PostgreSQL

## ORM
- SQLAlchemy

## Authentication
- JWT (JSON Web Tokens)

## Password Security
- bcrypt + passlib

---

# Roles

## Admin
- Full access
- Manage users
- Access admin dashboard

## Manager
- Manage workflows
- Assign tasks

## Employee
- Access own profile
- Work on assigned tasks

---

# Project Structure

```bash
workflow-management-system/
│
├── auth/
├── data/
├── models/
├── routes/
├── schemas/
├── services/
├── utils/
│
├── main.py
├── auth.py
├── database.py
├── requirements.txt
├── .env
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Takshsri/WorkFlow.git
```

```bash
cd workflow-management-system
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Create PostgreSQL database:

```sql
CREATE DATABASE workflow_db;
```

---

# Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/workflow_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256
```

---

# Run Server

```bash
uvicorn main:app --reload
```

Server runs on:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# Authentication APIs

## Signup

### POST `/signup`

```json
{
  "username": "admin",
  "email": "admin@gmail.com",
  "password": "1234",
  "role": "admin"
}
```

---

## Login

### POST `/login`

Returns JWT token.

---

# Protected Routes

## Get Profile

### GET `/profile`

Requires Bearer Token.

---

## Update Profile

### PATCH `/profile`

---

## Delete Profile

### DELETE `/profile`

---

# Admin Route

## GET `/admin-dashboard`

Accessible only for Admin role.

---

# Security Features

- JWT Authentication
- Password Hashing
- Protected Routes
- Role-Based Authorization
- Account Verification Checks
- Active Account Validation

---

# Future Enhancements

- Refresh Tokens
- Forgot Password System
- Email Verification
- Workflow Engine
- Task Assignment System
- Notifications
- AI Task Assistant
- Audit Logs
- Deployment

---

# Author

Ramya Mannam