from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/members", methods=['GET'])
def members():
    members = ["member1", "member2", "member3"]
    return jsonify({"members": members})


if __name__ == "__main__":
    # runs on port 5000
    app.run(debug=True)