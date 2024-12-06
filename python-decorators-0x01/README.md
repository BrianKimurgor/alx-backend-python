# Python Decorators Project

## **Overview**
This project focuses on mastering Python decorators by applying them to real-world database management tasks. By completing these tasks, you will enhance your ability to write reusable, efficient, and scalable code for handling database operations.

## **Learning Objectives**
By completing this project, you will:
1. Understand and implement Python decorators.
2. Automate database operations such as logging, connection handling, and transaction management.
3. Develop robust mechanisms for handling transient errors and caching results.
4. Learn best practices for writing maintainable and scalable Python applications.

---

## **Tasks and Instructions**

### **Task 0: Logging Database Queries**
- **Objective**: Create a `log_queries` decorator to log all SQL queries executed by a function.
- **Instructions**:
  - Implement the `log_queries` decorator.
  - The decorator should log the SQL query before it is executed.
- **File**: `0-log_queries.py`

Example usage:
```python
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
```

---

### **Task 1: Handle Database Connections with a Decorator**
- **Objective**: Implement a `with_db_connection` decorator to automatically handle opening and closing database connections.
- **Instructions**:
  - Pass a database connection to the decorated function.
  - Ensure the connection is properly closed after the function executes.
- **File**: `1-with_db_connection.py`

Example usage:
```python
@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()
```

---

### **Task 2: Transaction Management Decorator**
- **Objective**: Implement a `transactional` decorator to manage database transactions.
- **Instructions**:
  - Automatically commit or roll back transactions based on the function’s success or failure.
  - Use the `with_db_connection` decorator from Task 1.
- **File**: `2-transactional.py`

Example usage:
```python
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
```

---

### **Task 3: Retry Database Queries**
- **Objective**: Create a `retry_on_failure` decorator to retry database operations if they fail due to transient errors.
- **Instructions**:
  - Allow customization of the number of retries and delay between retries.
  - Use the `with_db_connection` decorator from Task 1.
- **File**: `3-retry_on_failure.py`

Example usage:
```python
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
```

---

### **Task 4: Cache Database Queries**
- **Objective**: Implement a `cache_query` decorator to cache the results of database queries.
- **Instructions**:
  - Use a global dictionary to store cached query results.
  - Optimize performance by returning cached results for duplicate queries.
- **File**: `4-cache_query.py`

Example usage:
```python
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
```

---

