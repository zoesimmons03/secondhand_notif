import mysql.connector as conn
import os
from dotenv import load_dotenv, dotenv_values
env_path = os.path.join(os.path.dirname(__file__), '.env')
sql_conn = {**dotenv_values(env_path)}

def create_connection():
    try:
        connection = conn.connect(
            host=sql_conn['host'],
            user=sql_conn['user'],
            password=sql_conn['password'],
            database=sql_conn['database']
        )
        if connection.is_connected():
            print("Connection to MySQL database established successfully.")
            return connection
    except conn.Error as err:
        print(f"Error: {err}")
        return None
    
print(create_connection())

