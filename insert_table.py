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

def insert_books(book_list):
    """Inserts multiple movies into the 'movie' table."""
    cursor = conn.cursor()
    query = "INSERT INTO movie (title, year) VALUES (%s, %s)"

    try:
        cursor.executemany(query, book_list)
        conn.commit()
        print(f"{cursor.rowcount} movies inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()

if __name__ == '__main__':
    books = [
        ('Harry Potter And The Order Of The Phoenix', '2021-03-12'),
        ('Gone with the Wind', '2025-12-11'),
        ('Pride and Prejudice (Modern Library Classics)', '2014-05-06')
    ]
    insert_books(books)

# Close the connection
conn.close()
