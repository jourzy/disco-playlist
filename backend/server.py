from flask import Flask, jsonify
from flask_cors import CORS
from db_utils import get_playlist

app = Flask(__name__)
CORS(app)

db_name = "db_disco_playlist"

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


if __name__ == "__main__":
    # runs on port 5000
    app.run(debug=True)