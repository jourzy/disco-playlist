import React from 'react';
import { useState } from 'react';

const Tracks = () => {
  const [query, setQuery] = useState("");
  const [tracks, setTracks] = useState([]);
  const [message, setMessage] = useState("");

  const searchTracks = async () => {
    if (!query) return;

    const response = await fetch(
      `http://localhost:5000/search?query=${encodeURIComponent(query)}`
    );

    const data = await response.json();
    setTracks(data.tracks?.items || []);
  };

  const addTrackToPlaylist = async (trackUri) => {
    const response = await fetch("http://localhost:5000/add_track", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ track_uri: trackUri }),
    });

    const data = await response.json();
    setMessage(data.message || data.error);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Spotify Track Search 🎵</h1>
      <input
        type="text"
        placeholder="Search for a track..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ padding: "10px", width: "300px", marginRight: "10px" }}
      />
      <button onClick={searchTracks} style={{ padding: "10px 20px" }}>
        Search
      </button>

      {message && <p style={{ color: "green" }}>{message}</p>}

      <ul style={{ marginTop: "20px", listStyle: "none", padding: 0 }}>
        {tracks.map((track) => (
          <li
            key={track.id}
            style={{
              marginBottom: "20px",
              borderBottom: "1px solid #ddd",
              paddingBottom: "10px",
            }}
          >
            <strong>{track.name}</strong> by{" "}
            {track.artists.map((artist) => artist.name).join(", ")}
            {track.album.images.length > 0 && (
              <img
                src={track.album.images[0].url}
                alt="Album cover"
                style={{ width: "50px", marginLeft: "10px" }}
              />
            )}
            {track.preview_url && (
              <audio controls style={{ display: "block", marginTop: "10px" }}>
                <source src={track.preview_url} type="audio/mpeg" />
                Your browser does not support audio playback.
              </audio>
            )}
            <button
              onClick={() => addTrackToPlaylist(track.uri)}
              style={{
                display: "block",
                marginTop: "10px",
                padding: "5px 10px",
                background: "green",
                color: "white",
                border: "none",
                cursor: "pointer",
              }}
            >
              Add to Playlist
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Tracks;