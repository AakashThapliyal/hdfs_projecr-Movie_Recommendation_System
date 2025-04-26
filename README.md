# Movie Recommendation System | Python, TMDb API, Hadoop HDFS | Tkinter GUI
A modern and intuitive Movie Recommendation App using Python, Tkinter, TMDb API, and HDFS integration for Big Data workflows.
Features
✅ Movie recommendation based on similar genres
✅ Clean and interactive Tkinter GUI
✅ Save recommended movies directly into Hadoop HDFS

How It Works
1. User inputs a movie name.
2. Fetches the movie’s ID and Genres using TMDb API.
3. Recommends top 5 popular movies within similar genres.
4. Displays recommendations in a popup window.
5. Allows saving the recommended list into HDFS at /movie/input/.

Installation and Setup
1. Clone the Repository
git clone https://github.com/yourusername/movierecommendationapp.git
cd movierecommendationapp
2. Install Required Packages
pip install requests
3. Set Up Hadoop HDFS (if not already done)
Start Hadoop services:
start-all.sh
4. Create HDFS directory:
hdfs dfs -mkdir -p /movie/input/
5. Run the Application
python movierecomendationapp.py

Requirements
1. Python 3.x
2. Hadoop with HDFS
3. Tkinter (comes built-in with Python)
4. Requests library (pip install requests)
