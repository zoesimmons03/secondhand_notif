import mysql.connector as conn


def create_connection():
    try:
        connection = conn.connect(
            host='zoes-MacBook-Air.local',
            user='root',
            password='Mywurld73!',
            database='drip_alert2000'
        )
        if connection.is_connected():
            print("Connection to MySQL database established successfully.")
            return connection
    except conn.Error as err:
        print(f"Error: {err}")
        return None
    
print(create_connection())