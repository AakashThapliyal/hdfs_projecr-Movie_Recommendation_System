# Movie Recommendation System | Python, TMDb API, Hadoop HDFS | Tkinter GUI
An interactive movie recommendation app built using Python and Tkinter that suggests similar movies based on TMDb genres. Integrated with HDFS to save recommendations for Big Data processing. Ideal for learning API integration, GUI development, and Hadoop interaction!
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
git clone [https://github.com/AakashThapliyal/hdfs_projecr-Movie_Recommendation_System.git]
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
