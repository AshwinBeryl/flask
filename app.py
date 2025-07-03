from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Database connection configuration
import os

db_config = {
    'host': os.getenv('DB_HOST', '172.31.19.73'),
    'user': os.getenv('DB_USER', 'flask'),
    'password': os.getenv('DB_PASSWORD', 'Flask@123'),
    'database': os.getenv('DB_NAME', 'blog')
}

# Function to create the database and table if they don't exist
def initialize_database():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Create database if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['database']}")
    cursor.execute(f"USE {db_config['database']}")

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS texts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content TEXT NOT NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

# Function to insert text into MySQL
def insert_text(text):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO texts (content) VALUES (%s)", (text,))
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_text = request.form.get('text')
        if user_text:
            insert_text(user_text)
    return '''<form method="POST">
                ENTER some TEXT: <input type="text" name="text">
                <input type="submit">
              </form>'''

if __name__ == '__main__':
    initialize_database()
    app.run(host="0.0.0.0", debug=True)