# Lab Three
Python script to create,read,update,delete (CRUD) a row from a **table**


# Run Locally

Clone the project

```bash
  git clone https://github.com/PLP-Database-DEPT/lab-3.git
```

Go to the project directory

```bash
  cd lab-3
```

Install dependencies

```bash
  python -m pip install -r requirements.txt
```

## Create Table
Hiding database base credentials instead of hard coding by setting the passwords as environment variables
(added this to all of the table code operations)
Install dotenv package
```bash
python -m pip install python-dotenv
```

Create a .env file
```bash
DB_USER=root
DB_PASSWORD=your_secret_password
```

Then add to `create_db.py` 
```bash
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
```

Make permananent for local development
```bash
export DB_USER="your_mysql_user"
export DB_PASSWORD="your_mysql_password"
```
Edited the code to create the tables in form of a dictionary and count all tables created by the code and sisplay the output
```bash
  python create_table.py
```

## Insert Table
Inserts tables innto the created tables 

```bash
  python insert_table.py
```

## Select Rows from a Table

```bash
  python select.py
```

## Update a row from a Table

```bash
  python update_table.py
```

## Delete a Row from a Table

```bash
  python delete_table.py
```

To be able to update the changes we made to this code, we need to fork the original repository
1. Click *fork* on the original repository
2. Get the fork URL
```bash
git remote set-url origin https://github.com/yourusername-forkedURL/repo.git
```
3. Check which branch we are on
```bash
git remote -v
```
4. Push the new code back to the forked branch/the fork
```bash
git push -u origin main
```
5. Double check to make sure all remote files match the files on your local repository. If not, check then add them using
```bash 
git status
git add README.md
git commit -m "Update README content"
git push -u origin main
```
6. Create a pull request on your fork on Github
- Click "Compare and pull request"
- Add a title/description and submit the PR
