# Flask Login & Signup System with MySQL

A simple Login and Signup Authentication System built using Flask and MySQL.

## Features

- User Registration
- User Login
- MySQL Database Integration
- Error Handling
- Responsive Frontend UI

---

## Technologies Used

- Python
- Flask
- MySQL
- HTML
- CSS
- JavaScript

---

## Project Structure

```text
Project/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── error.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
```

---

# Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/flask-login-system.git
```

```bash
cd flask-login-system
```

---

## Step 2: Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate Environment

```bash
venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

## Create Database

Open MySQL and execute:

```sql
CREATE DATABASE grrass;
```

Use database:

```sql
USE grrass;
```

---

## Create Table

```sql
CREATE TABLE students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);
```

---

## Verify Table

```sql
DESC students;
```

Expected Output:

| Field    | Type         |
|-----------|-------------|
| id        | int         |
| email     | varchar(100)|
| password  | varchar(100)|

---

# Configure Database Connection

Open app.py

Locate:

```python
conn = sql.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="grrass"
)
```

Replace:

```python
password="YOUR_PASSWORD"
```

with your MySQL password.

Example:

```python
password="Vrashbh@123"
```

---

# Running the Project

```bash
python app.py
```

Output:

```text
* Running on http://127.0.0.1:5000
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Signup Process

When user clicks Signup:

```python
INSERT INTO students(email,password)
VALUES(%s,%s)
```

This query inserts a new user into database.

Example:

```sql
INSERT INTO students(email,password)
VALUES('test@gmail.com','12345');
```

---

# Login Process

When user clicks Login:

```python
SELECT * FROM students
WHERE email=%s AND password=%s
```

This query checks whether the user exists.

Example:

```sql
SELECT * FROM students
WHERE email='test@gmail.com'
AND password='12345';
```

If record exists:

```text
Login Successful
```

Otherwise:

```text
Invalid Email or Password
```

---

# Useful SQL Queries

## Show Databases

```sql
SHOW DATABASES;
```

## Use Database

```sql
USE grrass;
```

## Show Tables

```sql
SHOW TABLES;
```

## View Users

```sql
SELECT * FROM students;
```

## Delete User

```sql
DELETE FROM students
WHERE id=1;
```

## Delete All Users

```sql
TRUNCATE TABLE students;
```

---

# Common Errors

## Access Denied

```text
Access denied for user 'root'
```

Solution:

Check MySQL password in app.py

---

## Database Not Found

```text
Unknown database 'grrass'
```

Solution:

```sql
CREATE DATABASE grrass;
```

---

## Table Not Found

```text
Table 'students' doesn't exist
```

Solution:

Run create table query again.

---

# Security Note

Current project stores passwords in plain text.

For production applications use:

- Werkzeug Password Hashing
- Flask-Login
- Session Authentication
- CSRF Protection

Example:

```python
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
```

---

# Author

Vrashbh Soni
