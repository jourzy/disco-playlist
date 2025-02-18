from flask import Flask, jsonify, request
import requests
import os
from flask_cors import CORS
from db_utils import get_playlist
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)

db_name = "db_disco_playlist"

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

@app.route("/playlist", methods=['GET'])
def playlist():
    try:
        # Fetch playlist data
        records = get_playlist(db_name)
        
        # Convert database records into a JSON-friendly format
        playlist_data = [
            {"Artist": row[0], "Song": row[1], "Votes": row[2]}
            for row in records
        ]

        return jsonify({"playlist": playlist_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error response
    

def get_access_token():
    """Get Spotify access token using Client Credentials Flow"""
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET), data=data)
    return response.json().get("access_token")

@app.route("/get_token")
def get_token():
    """Returns a Spotify API access token"""
    token = get_access_token()
    return jsonify({"access_token": token})

@app.route("/search", methods=["GET"])
def search_tracks():
    """Search for tracks on Spotify"""
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    token = get_access_token()
    url = f"https://api.spotify.com/v1/search?q={query}&type=track"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    return jsonify(response.json())


if __name__ == "__main__":
    # runs on port 5000
    app.run(debug=True)