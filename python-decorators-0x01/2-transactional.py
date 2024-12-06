import sqlite3
import functools

# Decorator to handle database connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open database connection
        conn = sqlite3.connect('users.db')
        try:
            # Pass the connection to the wrapped function
            result = func(conn, *args, **kwargs)
        finally:
            # Ensure the connection is closed after execution
            conn.close()
        return result
    return wrapper

# Decorator to handle transactions
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Execute the wrapped function
            result = func(conn, *args, **kwargs)
            # Commit the transaction if no errors
            conn.commit()
        except Exception as e:
            # Rollback the transaction on error
            conn.rollback()
            raise e
        return result
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
print("Email updated successfully!")
