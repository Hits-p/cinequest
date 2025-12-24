from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import requests

app = Flask(__name__)
CORS(app) 

# IMPORTANT: Put your real TMDB API key below!
TMDB_API_KEY = "c93f709551cbfbddfabe3b8133807fc8"  
# Host
# cinequest-db-hitansha-6d00.i.aivencloud.com

# Port
# 14696

# User
# avnadmin

# Password
# AVNS_wGfhWtUD1VgyAYUogWV



# SSL mode
# REQUIRED

# CA certificate

# Show
DB_CONFIG = {
    'host': 'cinequest-db-hitansha-6d00.i.aivencloud.com',
    'user': 'avnadmin',       # CHECK THIS: Your MySQL username
    'password': 'AVNS_wGfhWtUD1VgyAYUogWV', # CHECK THIS: Your MySQL password
    'database': 'cinequest_db',
    'port': 14696 ,
    'ssl_ca':'ca.pem'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/search', methods=['GET'])
def search_movies():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}"
    response = requests.get(url)
    return jsonify(response.json())

@app.route('/watchlist', methods=['POST'])
def add_to_watchlist():
    data = request.json
    user_id = data.get('user_id') 
    movie_id = data.get('movie_id')
    title = data.get('title')
    poster_path = data.get('poster_path')

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM watchlist WHERE user_id = %s AND movie_id = %s", (user_id, movie_id))
    if cursor.fetchone():
        return jsonify({"message": "Movie already in watchlist"}), 409

    cursor.execute(
        "INSERT INTO watchlist (user_id, movie_id, title, poster_path) VALUES (%s, %s, %s, %s)",
        (user_id, movie_id, title, poster_path)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Added to watchlist"}), 201

@app.route('/watchlist/<int:user_id>', methods=['GET'])
def get_watchlist(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM watchlist WHERE user_id = %s", (user_id,))
    movies = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True, port=5000)