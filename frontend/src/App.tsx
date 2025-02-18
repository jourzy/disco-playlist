import React, { JSX, useState } from 'react';
import disco_ball from './assets/disco_ball.png';
import './App.css';

function App(): JSX.Element {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState<any[]>([]); // Add state for search results

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  const handleSearchClick = async () => {
    const token = 'YOUR_SPOTIFY_ACCESS_TOKEN';
    const response = await fetch(`https://api.spotify.com/v1/search?q=${searchTerm}&type=track`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    const data = await response.json();
    setSearchResults(data.tracks.items);
  };

  return (
    <>
    <div className="homepage">
      <div className="introduction">
        <img src={disco_ball} className="discoball" alt="disco ball" />
        <h1>Welcome to Disco DJ</h1>
        <label htmlFor="search-input" className="search-label">Search for a song:</label>
        <input
            type="text"
            value={searchTerm}
            onChange={handleSearchChange}
            placeholder="Enter song name"
            className="search-input"
          />
          <button onClick={handleSearchClick} className="search-button">Search</button>
          </div>
          <div className="search-results">
            {searchResults.map((track) => (
              <div key={track.id}>
                {track.name} by {track.artists.map(artist => artist.name).join(', ')}
              </div>
            ))}
          </div>
    </div>  
    </>
  )
}

export default App
