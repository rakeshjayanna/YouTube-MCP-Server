from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# YouTube API credentials
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Home route
@app.route("/")
def home():
    return "YouTube MCP Server is running!"

# Search route
@app.route("/search", methods=["POST"])
def search_song():
    data = request.json
    song_name = data.get("song_name")

    if not song_name:
        return jsonify({"status": "error", "message": "Song name is missing"})

    # Search for the song using YouTube API
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": song_name,
        "type": "video",
        "maxResults": 1,
        "key": YOUTUBE_API_KEY
    }
    response = requests.get(search_url, params=params)
    search_results = response.json()

    # Check if the response contains videos
    if "items" not in search_results or not search_results["items"]:
        return jsonify({"status": "error", "message": f"No videos found for '{song_name}'"})

    # Get the first video's details
    video = search_results["items"][0]
    video_title = video["snippet"]["title"]
    video_id = video["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    return jsonify({
        "status": "success",
        "message": f"Found video: {video_title}",
        "video_title": video_title,
        "video_url": video_url
    })

# Run the server
if __name__ == "__main__":
    app.run(debug=True)