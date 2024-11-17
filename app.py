import mysql.connector
from mysql.connector import Error
import time

# Function to wait for MySQL to be available
def wait_for_mysql():
    while True:
        try:
            connection = mysql.connector.connect(
                host="mysql-service",  # MySQL service name in Kubernetes
                user="root",
                password="password",  # MySQL root password
                database="testdb"
            )
            if connection.is_connected():
                print("Connected to MySQL")
                connection.close()
                break
        except Error as e:
            print(f"Error: {e}, retrying...")
            time.sleep(5)

# Function to create the table in MySQL
def create_table():
    try:
        connection = mysql.connector.connect(
            host="mysql-service",  # MySQL service name in Kubernetes
            user="root",
            password="password",  # MySQL root password
            database="testdb"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100)
                )
            ''')
            print("Table created successfully")
        else:
            print("Failed to connect to the database")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    wait_for_mysql()  # Wait for MySQL to be ready
    create_table()    # Create the table in MySQL
