import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, ht, usr, pswd, db):
        """
        Initializes a new instance of the DatabaseConnection class.

        :param ht: Hostname or IP address of the database server.
        :param usr: Username to use for authentication.
        :param pswd: Password to use for authentication.
        :param db: Name of the database to connect to.
        """
        self.ht = ht
        self.usr = usr
        self.pswd = pswd
        self.db = db
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the database using the provided credentials.

        :return: A connection object if the connection is successful, None otherwise.
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
        except Error as e:
            print(f"Error trying to connect: {e}")
            self.connection = None
        return self.connection

    def close(self):
        """
        Closes the database connection if it is open.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Closed.")

    def __enter__(self):
        """
        Enables the use of the 'with' statement for this class.
        
        :return: The database connection object.
        """
        return self.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Ensures that the database connection is closed when exiting the 'with' block.
        """
        self.close()



def query_database():
    """
    Queries the 'users' table from the 'dental_clinic' database and prints each row.

    This function establishes a connection to the database using the DatabaseConnection
    context manager. It executes a SQL query to select all records from the 'users' table.
    The results are fetched and printed row by row. The database connection is automatically
    closed upon exiting the context manager.

    Note:
        Ensure that the DatabaseConnection class is defined and properly handles the
        connection to the database. The database credentials and host should be valid
        and secure.

    Raises:
        Any exceptions raised during the database connection or query execution will
        propagate up to the caller.
    """
    query = "SELECT * FROM users"
    
    with DatabaseConnection("localhost", "root", "Roniel@123", "dental_clinic") as connection:
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
            cursor.close()


query_database()