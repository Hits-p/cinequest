import mysql.connector

# 1. Connect to the "defaultdb" first (the lobby)
config = {
    'host': 'cinequest-db-hitansha-6d00.i.aivencloud.com',
    'user': 'avnadmin',
    'password': 'AVNS_wGfhWtUD1VgyAYUogWV',
    'database': 'defaultdb',  # We connect here first!
    'port': 14696,
    'ssl_ca': 'ca.pem'
}

try:
    print("1. Connecting to Aiven server...")
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    print("2. Creating database 'cinequest_db'...")
    cursor.execute("CREATE DATABASE IF NOT EXISTS cinequest_db")
    
    print("3. Switching to 'cinequest_db'...")
    cursor.execute("USE cinequest_db")

    print("4. Creating 'watchlist' table...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS watchlist (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        movie_id INT NOT NULL,
        title VARCHAR(255) NOT NULL,
        poster_path VARCHAR(255),
        UNIQUE KEY unique_movie_user (user_id, movie_id)
    )
    """)
    
    print("✅ SUCCESS! Database and Table created.")
    conn.close()

except Exception as e:
    print(f"❌ Error: {e}")