import mysql.connector

# PASTE YOUR NEW AIVEN DETAILS HERE
DB_CONFIG = {
    'host': 'YOUR_AIVEN_HOST_HERE',
    'user': 'avnadmin',
    'password': 'YOUR_AIVEN_PASSWORD',
    'database': 'defaultdb',
    'port': 12345
}

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # 1. Create Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    )
    """)
    print("Users table created.")

    # 2. Create Watchlist Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS watchlist (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        movie_id INT,
        title VARCHAR(255),
        poster_path VARCHAR(255),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)
    print("Watchlist table created.")

    # 3. Create the Dummy User (User #1)
    cursor.execute("""
    INSERT INTO users (username, email, password) 
    VALUES ('TestUser', 'test@test.com', 'password123')
    """)
    print("Test User created.")

    conn.commit()
    conn.close()
    print("SUCCESS! Cloud Database is ready.")

except Exception as e:
    print("Error:", e)