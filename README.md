# YouTube MCP Server

A Flask server that interacts with the YouTube Data API to search for songs and retrieve video links.

---

## Features
- Search for songs using the YouTube Data API.
- Retrieve video titles and URLs.
- Free to use (no Premium subscription required).

---

## Prerequisites
1. **Python 3.x**: Install from [python.org](https://www.python.org/downloads/).
2. **YouTube Data API Key**: Get it from the [Google Cloud Console](https://console.cloud.google.com/).

---

## Setup

### 1. Clone the Repository
git clone https://github.com/your-username/mcp-server.git
cd youtube-mcp-server

### 2. Set Up a Virtual Environment
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies
Install the required Python packages

### 4. Set Up Environment Variables
Create a .env file in the project folder.
Add your YouTube API key to the .env file:
YOUTUBE_API_KEY=your_api_key_here

### 5. Run the Server
Start the Flask server:python app.py
The server will run at http://localhost:5000.


### Usage
Search for a Song
Send a POST request to the /search endpoint with the following JSON body:
{
    "song_name": "Shape of You"
}

Example Response
If the song is found, the server will return:
{
    "status": "success",
    "message": "Found video: Shape of You - Ed Sheeran",
    "video_title": "Shape of You - Ed Sheeran",
    "video_url": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
}
If no results are found, the server will return:
{
    "status": "error",
    "message": "No videos found for 'Shape of You'"
}

### API Endpoints
GET /: Home page (returns "YouTube MCP Server is running!").

POST /search: Search for a song and retrieve video details.

### Contributing
Contributions are welcome! Follow these steps to contribute:
Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.

### Contact
For questions or feedback, feel free to reach out:
Your Name: rakeshjayanna19@gmail.com
GitHub: rakeshjayanna

