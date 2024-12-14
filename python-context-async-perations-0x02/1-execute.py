import mysql.connector
from mysql.connector import Error


class ExecuteQuery:
    """
    A class to handle database connections and execute queries.

    Attributes:
    ht (str): Hostname of the database server.
    usr (str): Username for database authentication.
    pswd (str): Password for database authentication.
    db (str): Database name to connect to.
    connection: Database connection object.
    cursor: Database cursor object.
    """

    def __init__(self, ht, usr, pswd, db):
        """
        Initializes the ExecuteQuery class with database connection parameters.

        Parameters:
        ht (str): Hostname of the database server.
        usr (str): Username for database authentication.
        pswd (str): Password for database authentication.
        db (str): Database name to connect to.
        """
        self.ht = ht
        self.usr = usr
        self.pswd = pswd
        self.db = db
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the database.

        Returns:
        ExecuteQuery: The instance of the class with an active database connection.

        Raises:
        Error: If there is an issue connecting to the database.
        """
        try:
            self.connection = mysql.connector.connect(
                ht=self.ht,
                usr=self.usr,
                psd=self.pswd,
                db=self.db
            )
            if self.connection.is_connected():
                print("Connected successfully to the database.")
                self.cursor = self.connection.cursor()
            
        except Error as e:
            print(f"Error trying connecting to: {e}")
            self.connection = None
            raise
        return self
    
    def execute_query(self, qry, param=None):
        """
        Executes a given SQL query with optional parameters.

        Parameters:
        qry (str): The SQL query to be executed.
        param (tuple, optional): Parameters to be used with the SQL query.

        Returns:
        list: The result of the query as a list of tuples. Returns an empty list if an error occurs.
        """
        try:
            self.cursor.execute(qry, param)
            return self.cursor.fetchall()
        except Error as e:
            return []
    
    def close(self):
        """
        Closes the database connection and cursor if they are open.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Closed.")

    def __enter__(self):
        """
        Enables the use of the class as a context manager. Calls the connect method.

        Returns:
        ExecuteQuery: The instance of the class with an active database connection.
        """
        return self.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Ensures that the cursor and connection are closed when exiting the context.

        Parameters:
        exc_type: The exception type.
        exc_value: The exception value.
        traceback: The traceback object.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()


#Context manager and the SELECT Query
def query_database():
    """
    Queries the database to retrieve all users older than 25 years.

    This function connects to the 'dental_clinic' database using the provided
    credentials and executes a SQL query to select all records from the 'users'
    table where the 'age' column is greater than 25. The results are then printed
    to the console.

    Note:
        Ensure that the 'ExecuteQuery' context manager is properly defined to handle
        database connections and query execution.

    Raises:
        Any exceptions raised during the database connection or query execution
        will propagate up to the caller.
    """
    qry = "SELECT * FROM users WHERE age > ?"
    param = (25,)
    
    with ExecuteQuery("localhost", "root", "Roniel@123", "dental_clinic") as db_manager:
        results = db_manager.execute_query(qry, param)
        print("Query Results:")
        for row in results:
            print(row)
