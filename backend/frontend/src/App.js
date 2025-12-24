import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; 

function App() {
  const [query, setQuery] = useState('');
  const [movies, setMovies] = useState([]);
  const [watchlist, setWatchlist] = useState([]);
  
  const USER_ID = 1; 

  const searchMovies = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.get(`http://localhost:5000/search?query=${query}`);
      setMovies(res.data.results);
    } catch (err) {
      console.error(err);
    }
  };

  const addToWatchlist = async (movie) => {
    try {
      await axios.post('http://localhost:5000/watchlist', {
        user_id: USER_ID,
        movie_id: movie.id,
        title: movie.title,
        poster_path: movie.poster_path
      });
      fetchWatchlist(); 
      alert("Movie added to Watchlist!");
    } catch (err) {
      alert("Movie is already in your watchlist!");
    }
  };

  const fetchWatchlist = async () => {
    try {
      const res = await axios.get(`http://localhost:5000/watchlist/${USER_ID}`);
      setWatchlist(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchWatchlist();
  }, []);

  return (
    <div className="App">
      
      {/* HEADER SECTION */}
      <header className="app-header">
        <h1>CineQuest 🎬</h1>
        <form onSubmit={searchMovies} className="search-container">
          <input 
            type="text" 
            className="search-input"
            placeholder="Search for movies..." 
            value={query} 
            onChange={(e) => setQuery(e.target.value)}
          />
          <button type="submit" className="search-btn">Search</button>
        </form>
      </header>

      {/* SEARCH RESULTS SECTION */}
      <div className="content-section">
        {movies.length > 0 && <h2>Search Results</h2>}
        
        <div className="movie-grid">
          {movies.map((movie) => (
            <div key={movie.id} className="movie-card">
              {movie.poster_path ? (
                 <img 
                   src={`https://image.tmdb.org/t/p/w300${movie.poster_path}`} 
                   alt={movie.title} 
                   className="movie-poster"
                 />
              ) : (
                <div className="no-image">No Image Available</div>
              )}
              
              <div className="movie-info">
                <h3>{movie.title}</h3>
                <button className="add-btn" onClick={() => addToWatchlist(movie)}>
                  + Add to Watchlist
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* WATCHLIST SECTION */}
      <div className="content-section" style={{marginTop: '50px'}}>
        <h2>My Watchlist</h2>
        {watchlist.length === 0 && <p style={{marginLeft: '40px', color: '#777'}}>No movies saved yet.</p>}
        
        <div className="movie-grid">
          {watchlist.map((item) => (
            <div key={item.id} className="movie-card">
              <img 
                src={`https://image.tmdb.org/t/p/w300${item.poster_path}`} 
                alt={item.title} 
                className="movie-poster"
              />
              <div className="movie-info">
                <h3>{item.title}</h3>
              </div>
            </div>
          ))}
        </div>
      </div>

    </div>
  );
}

export default App;