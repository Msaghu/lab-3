from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    database="movies",
    user=db_user,
    password=db_password
)

# Create a cursor object
cursor = conn.cursor()

# Execute the SQL statement to create the tables
tables = {
    "actors": """
    CREATE TABLE IF NOT EXISTS movie(
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(45),
        year date
    );
""",
    "movie": """
    CREATE TABLE IF NOT EXISTS actors(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(45),
        age INT
    );
"""
}

# Create tables
created_count = 0

for table_name, create_query in tables.items():
    cursor.execute(create_query)
    created_count += 1

# Commit the changes
conn.commit()

print(f"{created_count} tables created successfully")

# Close the connection
cursor.close()
conn.close()
