# Context Managers and Asynchronous Programming in Python

## Overview

This project focuses on learning and implementing **Context Managers** and **Asynchronous Programming** in Python. By the end of the project, you will have developed skills to effectively manage resources and execute concurrent database queries using both synchronous and asynchronous methods.

---

## Tasks

### 0. Custom Class-Based Context Manager for Database Connection
**Objective:**  
Create a class-based context manager to handle database connections automatically.

**Instructions:**  
- Define a class `DatabaseConnection` with:
  - `__enter__()` method: Handles opening the database connection.
  - `__exit__()` method: Closes the database connection.
- Use the context manager with a `with` statement to execute the query:  
  `SELECT * FROM users`
- Print the query results.

**File:**  
`0-databaseconnection.py`

---

### 1. Reusable Query Context Manager
**Objective:**  
Create a reusable context manager to execute any query with parameters while managing the connection.

**Instructions:**  
- Implement a class `ExecuteQuery` with:
  - `__enter__()` method: Opens the database connection and prepares the query.
  - `__exit__()` method: Closes the connection after execution.
- Input:  
  Query: `SELECT * FROM users WHERE age > ?`  
  Parameter: `25`  
- Return the result of the query.

**File:**  
`1-execute.py`

---

### 2. Concurrent Asynchronous Database Queries
**Objective:**  
Run multiple database queries concurrently using `asyncio.gather`.

**Instructions:**  
- Use the `aiosqlite` library for asynchronous SQLite operations.
- Implement:
  - `async_fetch_users()`: Fetch all users.
  - `async_fetch_older_users()`: Fetch users older than 40.
- Use `asyncio.gather()` to run the above functions concurrently.
- Create `fetch_concurrently()` and execute it with `asyncio.run()`.

**File:**  
`3-concurrent.py`

---

## Repository Structure

```plaintext
alx-backend-python/
└── python-context-async-perations-0x02/
    ├── 0-databaseconnection.py
    ├── 1-execute.py
    ├── 3-concurrent.py
```

---

## Requirements

- Python 3.8 or higher.
- Install `aiosqlite` for asynchronous operations:
  ```bash
  pip install aiosqlite
  ```
- Adhere to Python best practices and follow PEP 8 guidelines.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/alx-backend-python.git
   cd alx-backend-python/python-context-async-perations-0x02
   ```

2. Execute each script:
   ```bash
   python 0-databaseconnection.py
   python 1-execute.py
   python 3-concurrent.py
   ```

---