from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")


# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user=db_user,
    password=db_password
)

# Create a cursor object
cursor = conn.cursor()

# Create a new database
database_name = "movies" # Add a unique Database name
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

print(f"Database '{database_name}' created successfully!")

# Close the connection
cursor.close()
conn.close()


