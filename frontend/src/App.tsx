import React, { JSX, useState } from 'react';
import disco_ball from './assets/disco_ball.png';
import './App.css';
import Tracks from './components/Tracks';

interface Track {
  id: string;
  name: string;
  artists: { name: string }[];
  album: { images: { url: string }[] };
}

function App(): JSX.Element {
  const [songName, setSongName] = useState('');
  const [artistName, setArtistName] = useState('');
  const [searchResults, setSearchResults] = useState<Track[]>([]);

  const handleSongNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSongName(event.target.value);
  };

  const handleArtistNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setArtistName(event.target.value);
  };

  const handleSearchClick = async () => {
    const token = 'YOUR_SPOTIFY_ACCESS_TOKEN';
    const query = `${songName} ${artistName}`.trim().replace(/\s+/g, '+');
    const response = await fetch(`https://api.spotify.com/v1/search?q=${query}&type=track`, {
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
          <Tracks />
          <label htmlFor="song-name-input" className="search-label">Song name:</label>
          <input
            type="text"
            id="song-name-input"
            value={songName}
            onChange={handleSongNameChange}
            placeholder="Enter song name"
            className="search-input"
          />
          <label htmlFor="artist-name-input" className="search-label">Artist name:</label>
          <input
            type="text"
            id="artist-name-input"
            value={artistName}
            onChange={handleArtistNameChange}
            placeholder="Enter artist name"
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
  );
}

export default App;
